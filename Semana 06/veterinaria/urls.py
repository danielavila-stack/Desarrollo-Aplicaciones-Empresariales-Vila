from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # Redirige la ruta vacía "/veterinaria/" al listado de especies
    path('', RedirectView.as_view(pattern_name='lista_especies', permanent=False)),
    
    # Especies
    path('especies/', views.lista_especies, name='lista_especies'),
    path('especies/crear/', views.crear_especie, name='crear_especie'),
    path('especies/<int:pk>/editar/', views.editar_especie, name='editar_especie'),
    path('especies/<int:pk>/eliminar/', views.eliminar_especie, name='eliminar_especie'),
    
    # Insumos
    path('insumos/', views.lista_insumos, name='lista_insumos'),
    path('insumos/crear/', views.crear_insumo, name='crear_insumo'),
    path('insumos/<int:pk>/editar/', views.editar_insumo, name='editar_insumo'),
    path('insumos/<int:pk>/eliminar/', views.eliminar_insumo, name='eliminar_insumo'),
    
    # Servicios
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    
    # Mascotas
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/<int:pk>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/<int:pk>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),
    
    # Historiales
    path('historiales/', views.lista_historiales, name='lista_historiales'),
    path('historiales/crear/', views.crear_historial, name='crear_historial'),
    path('historiales/<int:pk>/editar/', views.editar_historial, name='editar_historial'),
    path('historiales/<int:pk>/eliminar/', views.eliminar_historial, name='eliminar_historial'),

    # Consultas de negocio
    path('citas/', views.lista_citas, name='cita_list'),
    path('citas/crear/', views.crear_cita, name='crear_cita'),
    path('recetas/', views.lista_recetas, name='receta_list'),
    path('recetas/detalles/', views.lista_detalles, name='lista_detalles'),
    path('recetas/detalles/crear/', views.crear_detalle, name='crear_detalle'),
    path('recetas/detalles/<int:pk>/editar/', views.editar_detalle, name='editar_detalle'),
    path('recetas/detalles/<int:pk>/eliminar/', views.eliminar_detalle, name='eliminar_detalle'),
]