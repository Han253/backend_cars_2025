from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)       # Marca
    model = models.CharField(max_length=100)       # Modelo
    year = models.PositiveIntegerField()           # Año de fabricación
    price = models.DecimalField(max_digits=12, decimal_places=2) # Precio
    mileage = models.PositiveIntegerField()        # Kilometraje
    description = models.TextField(blank=True)   # Descripción
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    city = models.CharField(max_length=100)     # Municipio
    state = models.CharField(max_length=100)    # Departamento
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
