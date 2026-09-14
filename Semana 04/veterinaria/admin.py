from django.contrib import admin

from .models import (
	CitaMedica,
	DetalleReceta,
	Factura,
	FichaMedica,
	PerfilVeterinario,
)


admin.site.register([
	PerfilVeterinario,
	FichaMedica,
	CitaMedica,
	DetalleReceta,
	Factura,
])
