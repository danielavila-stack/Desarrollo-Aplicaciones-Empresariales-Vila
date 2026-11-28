from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Categoria, Producto


class ProductoApiTests(TestCase):
    def setUp(self):
        self.client_api = APIClient()
        self.categoria = Categoria.objects.create(nombre="Antiparasitarios")
        self.producto = Producto.objects.create(
            nombre="Pipeta para perros",
            precio=Decimal("35.90"),
            stock=4,
            categoria=self.categoria,
        )

    def test_lista_incluye_el_nombre_de_categoria(self):
        respuesta = self.client_api.get("/api/productos/")

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.data[0]["categoria_nombre"], "Antiparasitarios")

    def test_no_acepta_precio_cero(self):
        respuesta = self.client_api.post(
            "/api/productos/",
            {
                "nombre": "Vacuna veterinaria",
                "precio": "0.00",
                "stock": 2,
                "activo": True,
                "categoria": self.categoria.id,
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.assertEqual(Producto.objects.count(), 1)
