from django.contrib import admin
from .models import (
    Especie,
    Insumo,
    Servicio,
    Mascota,
    HistorialMedico,
    PerfilVeterinario,
    FichaMedica,
    CitaMedica,
    DetalleReceta,
    Factura,
)

# ===================================================
# INLINES (Relaciones)
# ===================================================

# Ejercicio 6: StackedInline (Relación 1:1 -> FichaMedica dentro de Mascota)

class FichaMedicaInline(admin.StackedInline):
    model = FichaMedica
    extra = 1  # Muestra 1 formulario en bloque


# Ejercicio 7: TabularInline (Relación N:M -> DetalleReceta dentro de CitaMedica)

class DetalleRecetaInline(admin.TabularInline):
    model = DetalleReceta
    extra = 1  # Muestra filas estilo tabla


# ===================================================
# REGISTRO Y PERSONALIZACIÓN DE MODELOS
# ===================================================

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'edad', 'dueno_nombre')
    search_fields = ('nombre', 'dueno_nombre')
    inlines = [FichaMedicaInline]  # Inyecta la Ficha Médica 1:1


@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'veterinario', 'fecha_hora', 'estado', 'motivo')
    list_display_links = ('id', 'mascota')  # <-- Hace que el ID y la Mascota sean enlaces
    search_fields = ('motivo', 'mascota__nombre')
    list_filter = ('estado', 'fecha_hora')
    inlines = [DetalleRecetaInline]


@admin.register(PerfilVeterinario)
class PerfilVeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'colegiatura', 'especialidad', 'telefono')
    search_fields = ('colegiatura', 'especialidad', 'usuario__username')


@admin.register(FichaMedica)
class FichaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'codigo_chip', 'grupo_sanguineo')
    search_fields = ('codigo_chip', 'mascota__nombre')
    list_filter = ('grupo_sanguineo',)


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'historial', 'total', 'fecha_emision', 'pagado')
    search_fields = ('historial__mascota__nombre',)
    list_filter = ('pagado', 'fecha_emision')


@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'fecha', 'diagnostico')
    search_fields = ('diagnostico', 'tratamiento', 'mascota__nombre')
    list_filter = ('fecha',)


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'precio')
    search_fields = ('nombre',)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio')


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(DetalleReceta)
class DetalleRecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cita', 'insumo', 'cantidad')