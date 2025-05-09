from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Car
from django.contrib.auth.models import User

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['created_at']  # Excluir el campo created_at


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# Para personalizar el token JWT
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Añadir campos personalizados al payload del token
        token['username'] = user.username
        token['email'] = user.email

        return token