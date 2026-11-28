from rest_framework import filters, viewsets

from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    # Obtiene productos y su categoría en una sola consulta relacionada.
    queryset = Producto.objects.select_related("categoria").all()
    # Convierte los productos a JSON y valida las escrituras de la API.
    serializer_class = ProductoSerializer
    # Habilita búsquedas con el parámetro ?search=.
    filter_backends = [filters.SearchFilter]
    # Busca tanto en el nombre del producto como en el nombre de categoría.
    search_fields = ["nombre", "categoria__nombre"]
