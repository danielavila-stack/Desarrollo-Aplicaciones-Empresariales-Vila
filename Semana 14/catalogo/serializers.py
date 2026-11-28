from rest_framework import serializers

from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    # Expone el nombre de la categoría sin permitir editarlo desde este campo.
    categoria_nombre = serializers.CharField(source="categoria.nombre", read_only=True)

    class Meta:
        # Define el modelo que el serializador transforma a JSON y viceversa.
        model = Producto
        # Incluye el identificador de categoría para crear y editar productos.
        fields = (
            "id",
            "nombre",
            "precio",
            "stock",
            "activo",
            "categoria",
            "categoria_nombre",
        )

    def validate_precio(self, value):
        # Rechaza precios que no representen un importe de venta positivo.
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return value
