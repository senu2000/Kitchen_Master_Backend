from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer
from .serializers import RecipeSerializer

from .models import User
from .models import Recipe

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User added successfully")
        return JsonResponse("Fail to add user", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("User is deleted successfully", safe=False)


class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


@csrf_exempt
def recipeApi(request, id=0):
    if request.method == 'GET':
        recipe = Recipe.objects.all()
        recipe_serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse(recipe_serializer.data, safe=False)
    elif request.method == 'POST':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Recipe added successfully")
        return JsonResponse("Fail to add recipe", safe=False)
    elif request.method == 'DELETE':
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return JsonResponse("Recipe is deleted successfully", safe=False)
    elif request.method == 'PUT':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(Recipe, data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Recipe updated successfully")
        return JsonResponse("Fail to update recipe", safe=False)
