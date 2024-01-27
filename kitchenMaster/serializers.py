from rest_framework import serializers
from .models import User
from .models import Recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
