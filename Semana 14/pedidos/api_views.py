from decimal import Decimal

from django.db import transaction
from django.db.models import F
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from catalogo.models import Producto

from .models import Cliente, DetallePedido, Pago, Pedido


@api_view(["POST"])
def crear_pedido(request):
    # Valida que el cuerpo tenga identificador de cliente y una lista de artículos.
    if not isinstance(request.data, dict):
        raise serializers.ValidationError(
            "El cuerpo de la solicitud debe ser un objeto JSON."
        )
    cliente_id = request.data.get("cliente_id")
    items = request.data.get("items")
    if isinstance(cliente_id, bool) or not isinstance(cliente_id, int):
        raise serializers.ValidationError(
            {"cliente_id": "Debe indicar un identificador de cliente entero."}
        )
    if not isinstance(items, list) or not items:
        raise serializers.ValidationError(
            {"items": "Debe incluir al menos un producto."}
        )

    # Consolida productos repetidos para validar y descontar la cantidad total.
    cantidades = {}
    for indice, item in enumerate(items):
        if not isinstance(item, dict):
            raise serializers.ValidationError(
                {"items": f"El elemento {indice} debe ser un objeto."}
            )
        producto_id = item.get("producto_id")
        cantidad = item.get("cantidad")
        if isinstance(producto_id, bool) or not isinstance(producto_id, int):
            raise serializers.ValidationError(
                {"items": f"El producto del elemento {indice} no es válido."}
            )
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise serializers.ValidationError(
                {"items": f"La cantidad del elemento {indice} debe ser mayor que cero."}
            )
        cantidades[producto_id] = cantidades.get(producto_id, 0) + cantidad

    # Agrupa las lecturas, descuentos y creación del pedido en una transacción.
    with transaction.atomic():
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError(
                {"cliente_id": "El cliente indicado no existe."}
            )

        productos = []
        for producto_id, cantidad in cantidades.items():
            try:
                producto = Producto.objects.select_for_update().get(pk=producto_id)
            except Producto.DoesNotExist:
                raise serializers.ValidationError(
                    {"producto_id": f"El producto {producto_id} no existe."}
                )
            if not producto.activo:
                raise serializers.ValidationError(
                    {"producto_id": f"El producto '{producto.nombre}' está inactivo."}
                )
            if producto.stock < cantidad:
                raise serializers.ValidationError(
                    {
                        "stock": (
                            f"Stock insuficiente para '{producto.nombre}': "
                            f"disponibles {producto.stock}, solicitados {cantidad}."
                        )
                    }
                )
            productos.append((producto, cantidad))

        # Descuenta stock con F y condición para evitar cantidades negativas.
        for producto, cantidad in productos:
            actualizado = Producto.objects.filter(
                pk=producto.pk,
                stock__gte=cantidad,
            ).update(stock=F("stock") - cantidad)
            if actualizado != 1:
                raise serializers.ValidationError(
                    {"stock": f"Stock insuficiente para '{producto.nombre}'."}
                )

        # Calcula el total usando los precios actuales leídos desde la base de datos.
        total = sum(
            (producto.precio * cantidad for producto, cantidad in productos),
            Decimal("0.00"),
        )
        pedido = Pedido.objects.create(cliente=cliente, total=total)
        for producto, cantidad in productos:
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio,
            )

    # Devuelve el resumen creado, sin aceptar precios aportados por el cliente.
    return Response(
        {
            "id": pedido.id,
            "total": str(pedido.total),
            "estado": pedido.estado,
        },
        status=status.HTTP_201_CREATED,
    )


@api_view(["POST"])
def pagar_pedido(request, pedido_id):
    # Impide recibir datos de tarjeta; el flujo solo acepta el token simulado.
    if not isinstance(request.data, dict):
        raise serializers.ValidationError(
            "El cuerpo de la solicitud debe ser un objeto JSON."
        )
    if set(request.data) - {"token"}:
        raise serializers.ValidationError(
            "Envíe únicamente el token simulado; no se reciben datos de tarjeta."
        )

    # Valida el token que representa la respuesta de la pasarela simulada.
    token = request.data.get("token")
    if (
        not isinstance(token, str)
        or not token.strip()
        or not token.strip().startswith("tok_sim_")
    ):
        raise serializers.ValidationError(
            {"token": "Debe proporcionar un token simulado con prefijo tok_sim_."}
        )

    # Bloquea el pedido y registra el pago junto al cambio de estado atómicamente.
    with transaction.atomic():
        try:
            pedido = Pedido.objects.select_for_update().get(pk=pedido_id)
        except Pedido.DoesNotExist:
            raise NotFound("El pedido indicado no existe.")
        if pedido.estado == Pedido.Estado.PAGADO:
            raise serializers.ValidationError(
                {"pedido": "El pedido ya está pagado."}
            )
        if pedido.estado != Pedido.Estado.PENDIENTE_PAGO:
            raise serializers.ValidationError(
                {"pedido": "El pedido no está pendiente de pago."}
            )

        pago = Pago.objects.create(
            pedido=pedido,
            monto=pedido.total,
            estado=Pago.Estado.APROBADO,
            referencia=token.strip(),
        )
        pedido.estado = Pedido.Estado.PAGADO
        pedido.save(update_fields=["estado"])

    # Confirma el resultado de la simulación sin exponer información de tarjeta.
    return Response(
        {
            "pedido_id": pedido.id,
            "monto": str(pago.monto),
            "estado_pago": pago.estado,
            "estado_pedido": pedido.estado,
            "referencia": pago.referencia,
        },
        status=status.HTTP_200_OK,
    )
