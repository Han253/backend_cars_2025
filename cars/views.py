from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .serializers import CarSerializer


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()  # Queryset que define todos los carros disponibles
    serializer_class = CarSerializer  # Serializador que se usará para este modelo

    # Opcionalmente, puedes personalizar filtros, permisos o acciones aquí.
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'model', 'year', 'city', 'state']  # Campos por los que se puede filtrar


