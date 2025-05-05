from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, RegisterView

# Crear un enrutador y registrar el viewset de Car
router = DefaultRouter()
router.register(r'cars', CarViewSet)

# Incluir las URLs del enrutador en las rutas del proyecto
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
