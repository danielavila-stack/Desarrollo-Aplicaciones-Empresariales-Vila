from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio


class VeterinariaFlowTests(TestCase):
    def test_catalogos_y_actualizaciones(self):
        self.client.post(reverse('veterinaria:especie_create'), {'nombre': 'Canino'})
        self.client.post(reverse('veterinaria:insumo_create'), {'nombre': 'Vacuna', 'stock': 10, 'precio': '25.50'})
        self.client.post(reverse('veterinaria:servicio_create'), {'nombre': 'Consulta', 'precio': '40.00'})

        insumo = Insumo.objects.get(nombre='Vacuna')
        servicio = Servicio.objects.get(nombre='Consulta')
        self.client.post(reverse('veterinaria:insumo_update', args=[insumo.pk]), {'nombre': 'Vacuna', 'stock': 8, 'precio': '30.00'})
        self.client.post(reverse('veterinaria:servicio_update', args=[servicio.pk]), {'nombre': 'Consulta general', 'precio': '45.00'})

        self.assertEqual(Insumo.objects.get(pk=insumo.pk).precio, Decimal('30.00'))
        self.assertEqual(Servicio.objects.get(pk=servicio.pk).nombre, 'Consulta general')
        self.assertContains(self.client.get(reverse('veterinaria:especie_list') + '?q=can'), 'Canino')

    def test_historial_requiere_mascota_y_elimina_con_mascota(self):
        mascota = Mascota.objects.create(nombre='Luna', edad=3, dueno_nombre='Ana Torres')
        response = self.client.post(reverse('veterinaria:historial_create'), {
            'mascota': mascota.pk,
            'fecha': date.today().isoformat(),
            'diagnostico': 'Control general',
            'tratamiento': 'Vitaminas',
        })

        self.assertRedirects(response, reverse('veterinaria:historial_list'))
        self.assertEqual(HistorialMedico.objects.count(), 1)
        self.assertContains(self.client.get(reverse('veterinaria:historial_list') + '?q=control'), 'Luna')

        mascota.delete()
        self.assertEqual(HistorialMedico.objects.count(), 0)

    def test_mascota_se_actualiza_y_elimina_por_post(self):
        mascota = Mascota.objects.create(nombre='Max', edad=2, dueno_nombre='Luis Perez')
        self.client.post(reverse('veterinaria:mascota_update', args=[mascota.pk]), {
            'nombre': 'Maximus', 'edad': 4, 'dueno_nombre': 'Luis Perez'
        })
        self.assertEqual(Mascota.objects.get(pk=mascota.pk).nombre, 'Maximus')

        response = self.client.post(reverse('veterinaria:mascota_delete', args=[mascota.pk]))
        self.assertRedirects(response, reverse('veterinaria:mascota_list'))
        self.assertFalse(Mascota.objects.filter(pk=mascota.pk).exists())
