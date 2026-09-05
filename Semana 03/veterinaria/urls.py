from django.urls import path

from . import views

app_name = 'veterinaria'

urlpatterns = [
    path('', views.mascota_list, name='home'),
    path('especies/', views.especie_list, name='especie_list'),
    path('especies/nueva/', views.especie_create, name='especie_create'),
    path('especies/<int:pk>/editar/', views.especie_update, name='especie_update'),
    path('especies/<int:pk>/eliminar/', views.especie_delete, name='especie_delete'),
    path('insumos/', views.insumo_list, name='insumo_list'),
    path('insumos/nuevo/', views.insumo_create, name='insumo_create'),
    path('insumos/<int:pk>/editar/', views.insumo_update, name='insumo_update'),
    path('insumos/<int:pk>/eliminar/', views.insumo_delete, name='insumo_delete'),
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicios/nuevo/', views.servicio_create, name='servicio_create'),
    path('servicios/<int:pk>/editar/', views.servicio_update, name='servicio_update'),
    path('servicios/<int:pk>/eliminar/', views.servicio_delete, name='servicio_delete'),
    path('mascotas/', views.mascota_list, name='mascota_list'),
    path('mascotas/nueva/', views.mascota_create, name='mascota_create'),
    path('mascotas/<int:pk>/editar/', views.mascota_update, name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', views.mascota_delete, name='mascota_delete'),
    path('historiales/', views.historial_list, name='historial_list'),
    path('historiales/nuevo/', views.historial_create, name='historial_create'),
    path('historiales/<int:pk>/editar/', views.historial_update, name='historial_update'),
    path('historiales/<int:pk>/eliminar/', views.historial_delete, name='historial_delete'),
]
