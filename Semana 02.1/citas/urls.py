from django.urls import path

from . import views


app_name = 'citas'

urlpatterns = [
    path('', views.lista_citas_view, name='lista'),
    path('nueva/', views.crear_cita_view, name='crear'),
    path('cita/<int:cita_id>/', views.detalle_cita_view, name='detalle'),
    path('cita/<int:cita_id>/estado/', views.cambiar_estado_view, name='cambiar_estado'),
    path('cita/<int:cita_id>/eliminar/', views.eliminar_cita_view, name='eliminar'),
]