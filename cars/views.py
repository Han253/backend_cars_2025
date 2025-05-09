from rest_framework import viewsets, filters, generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import Car
from .serializers import CarSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from .filters import CarFilter


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()  # Queryset que define todos los carros disponibles
    serializer_class = CarSerializer  # Serializador que se usará para este modelo

    # Opcionalmente, puedes personalizar filtros, permisos o acciones aquí.
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CarFilter  # Filtros personalizados para el modelo Car

    # Campos permitidos para ordenar
    ordering_fields = ['price', 'year', 'mileage', 'created_at']
    ordering = ['-created_at']  # Orden predeterminado


# RegisterView es la vista para el registro de usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# CustomTokenObtainPairView es la vista para obtener el token JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer