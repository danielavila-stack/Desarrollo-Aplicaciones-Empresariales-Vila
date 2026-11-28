from django.urls import path

from . import api_views

urlpatterns = [
    path("pedidos/crear/", api_views.crear_pedido, name="crear-pedido"),
    path(
        "pedidos/<int:pedido_id>/pagar/",
        api_views.pagar_pedido,
        name="pagar-pedido",
    ),
]
