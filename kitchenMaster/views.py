from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer , RecipeAddSerializer , UserSerializer

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

class OneUserView(APIView):
    def get(self, request, email):
        try:
            user = User.objects.get(email=email)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

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
            return JsonResponse("User added successfully", safe=False)
        return JsonResponse("Fail to add user", safe=False)

class FindUser(APIView):
    def get(self , request):
        return(Response({
            "details":request.user.is_superuser
        }))

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

class OneRecipeView(APIView):
    def get(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
            recipe_serializer = RecipeSerializer(recipe)
            return JsonResponse(recipe_serializer.data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=404)


class RecipeViewUsingFk(APIView):
    def get(self, request, fk_id):
        try:
            recipes = Recipe.objects.filter(fk_id=fk_id)
            recipe_serializer = RecipeSerializer(recipes, many=True)
            return JsonResponse(recipe_serializer.data, safe=False)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=404)


class RecipeDeleteView(APIView):
    def delete(self, request, id):
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return JsonResponse("details : success", safe=False)


class RecipeAddView(APIView):
    def post(self, request):
        recipe_serializer = RecipeAddSerializer(data=request.data)

        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return Response("Recipe added successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
