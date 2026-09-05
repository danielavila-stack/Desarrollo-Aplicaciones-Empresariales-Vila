from django.contrib import admin

from .models import Especie, HistorialMedico, Insumo, Mascota, Servicio

admin.site.register([Especie, Insumo, Servicio, Mascota, HistorialMedico])
