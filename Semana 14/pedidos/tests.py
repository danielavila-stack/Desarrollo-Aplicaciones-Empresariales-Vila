from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from catalogo.models import Categoria, Producto

from .models import Cliente, DetallePedido, Pago, Pedido


class PedidoApiTests(TestCase):
    def setUp(self):
        self.client_api = APIClient()
        self.cliente = Cliente.objects.create(
            nombre="María López",
            email="maria@example.com",
            telefono="555123456",
        )
        self.categoria = Categoria.objects.create(nombre="Productos de prueba")
        self.producto = Producto.objects.create(
            nombre="Antiparasitario para perros",
            precio=Decimal("35.90"),
            stock=5,
            categoria=self.categoria,
        )

    def test_crea_pedido_y_descuenta_stock_con_precio_de_bd(self):
        respuesta = self.client_api.post(
            "/api/pedidos/crear/",
            {
                "cliente_id": self.cliente.id,
                "items": [
                    {
                        "producto_id": self.producto.id,
                        "cantidad": 2,
                        "precio": "0.01",
                    }
                ],
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 201)
        self.assertEqual(respuesta.data["total"], "71.80")
        self.assertEqual(respuesta.data["estado"], Pedido.Estado.PENDIENTE_PAGO)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 3)
        detalle = DetallePedido.objects.get(pedido_id=respuesta.data["id"])
        self.assertEqual(detalle.precio_unitario, self.producto.precio)

    def test_stock_insuficiente_no_crea_pedido_ni_modifica_stock(self):
        producto_agotado = Producto.objects.create(
            nombre="Vacuna agotada",
            precio=Decimal("48.00"),
            stock=0,
            categoria=self.categoria,
        )
        respuesta = self.client_api.post(
            "/api/pedidos/crear/",
            {
                "cliente_id": self.cliente.id,
                "items": [
                    {"producto_id": self.producto.id, "cantidad": 2},
                    {"producto_id": producto_agotado.id, "cantidad": 1},
                ],
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.producto.refresh_from_db()
        producto_agotado.refresh_from_db()
        self.assertEqual(self.producto.stock, 5)
        self.assertEqual(producto_agotado.stock, 0)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_producto_inactivo_no_crea_pedido_ni_descuenta_stock(self):
        self.producto.activo = False
        self.producto.save(update_fields=["activo"])

        respuesta = self.client_api.post(
            "/api/pedidos/crear/",
            {
                "cliente_id": self.cliente.id,
                "items": [{"producto_id": self.producto.id, "cantidad": 1}],
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 5)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_producto_inexistente_no_crea_pedido(self):
        respuesta = self.client_api.post(
            "/api/pedidos/crear/",
            {
                "cliente_id": self.cliente.id,
                "items": [{"producto_id": 9999, "cantidad": 1}],
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(self.producto.stock, 5)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_pago_aprueba_y_actualiza_el_pedido(self):
        respuesta_pedido = self.client_api.post(
            "/api/pedidos/crear/",
            {
                "cliente_id": self.cliente.id,
                "items": [{"producto_id": self.producto.id, "cantidad": 1}],
            },
            format="json",
        )
        respuesta_pago = self.client_api.post(
            f"/api/pedidos/{respuesta_pedido.data['id']}/pagar/",
            {"token": "tok_sim_123"},
            format="json",
        )

        self.assertEqual(respuesta_pago.status_code, 200)
        self.assertEqual(respuesta_pago.data["estado_pago"], Pago.Estado.APROBADO)
        self.assertEqual(respuesta_pago.data["estado_pedido"], Pedido.Estado.PAGADO)
        pedido = Pedido.objects.get(pk=respuesta_pedido.data["id"])
        self.assertEqual(pedido.estado, Pedido.Estado.PAGADO)
        self.assertEqual(pedido.pago.monto, pedido.total)
        self.assertEqual(pedido.pago.referencia, "tok_sim_123")

    def test_pedido_pagado_no_acepta_un_segundo_pago(self):
        pedido = Pedido.objects.create(cliente=self.cliente, total=Decimal("35.90"))
        respuesta_primera = self.client_api.post(
            f"/api/pedidos/{pedido.id}/pagar/",
            {"token": "tok_sim_123"},
            format="json",
        )
        respuesta_repetida = self.client_api.post(
            f"/api/pedidos/{pedido.id}/pagar/",
            {"token": "tok_sim_456"},
            format="json",
        )

        self.assertEqual(respuesta_primera.status_code, 200)
        self.assertEqual(respuesta_repetida.status_code, 400)
        self.assertEqual(Pago.objects.filter(pedido=pedido).count(), 1)

    def test_pago_rechaza_datos_de_tarjeta(self):
        pedido = Pedido.objects.create(cliente=self.cliente, total=Decimal("35.90"))

        respuesta = self.client_api.post(
            f"/api/pedidos/{pedido.id}/pagar/",
            {"token": "tok_sim_123", "cvv": "123"},
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.assertFalse(Pago.objects.filter(pedido=pedido).exists())
