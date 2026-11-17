from rest_framework import status
from rest_framework.test import APITestCase


class ServicioApiTests(APITestCase):
    def test_lista_y_busqueda_de_servicios(self):
        self.client.post(
            '/api/servicios/',
            {'nombre': 'Consulta general', 'precio': '30.00'},
            format='json',
        )

        respuesta = self.client.get('/api/servicios/', {'search': 'Consulta'})

        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(respuesta.data), 1)
        self.assertEqual(respuesta.data[0]['nombre'], 'Consulta general')

    def test_rechaza_precio_cero_y_crea_servicio_valido(self):
        invalido = self.client.post(
            '/api/servicios/',
            {'nombre': 'Prueba', 'precio': '0.00'},
            format='json',
        )
        valido = self.client.post(
            '/api/servicios/',
            {'nombre': 'Vacunación', 'precio': '25.00'},
            format='json',
        )

        self.assertEqual(invalido.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(valido.status_code, status.HTTP_201_CREATED)

    def test_actualiza_y_elimina_servicio(self):
        creado = self.client.post(
            '/api/servicios/',
            {'nombre': 'Consulta', 'precio': '30.00'},
            format='json',
        )
        url = f"/api/servicios/{creado.data['id']}/"

        actualizado = self.client.patch(
            url,
            {'nombre': 'Consulta revisada'},
            format='json',
        )
        eliminado = self.client.delete(url)

        self.assertEqual(actualizado.status_code, status.HTTP_200_OK)
        self.assertEqual(actualizado.data['nombre'], 'Consulta revisada')
        self.assertEqual(eliminado.status_code, status.HTTP_204_NO_CONTENT)
