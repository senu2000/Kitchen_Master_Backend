from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .serializers import UserSerializer
from .serializers import RecipeSerializer

from .models import User
from .models import Recipe

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


# Create your views here.
class UserView(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)


class UserDeleteView(APIView):
    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("details : success", safe=False)


class UserAddView(APIView):
    def post(self, request):
        # user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User added successfully")
        return JsonResponse("Fail to add user", safe=False)


class RecipeUpdate(APIView):
    def put(self, request):
        try:
            instance = Recipe.objects.get(id=request.data.get("id"))
            serializer = RecipeSerializer(
                instance,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse("success", safe=False)
        except:
            return JsonResponse("Fail to update1 recipe", safe=False)


class RecipeView(APIView):
    def get(self, request):
        recipe = Recipe.objects.all()
        recipe_serializer = RecipeSerializer(recipe, many=True)
        return JsonResponse(recipe_serializer.data, safe=False)

class RecipeDeleteView(APIView):
    def delete(self, request, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return JsonResponse("details : success", safe=False)

class RecipeAddView(APIView):
    def post(self, request):
        recipe = Recipe.objects.all()
        recipe_serializer = RecipeSerializer(recipe, many=True)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Recipe added successfully")
        return JsonResponse("Fail to add user", safe=False)