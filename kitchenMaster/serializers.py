from rest_framework import serializers
from .models import User
from .models import Recipe
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        # token for user account and hashing password
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
