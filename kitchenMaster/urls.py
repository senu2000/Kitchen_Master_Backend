from django.urls import path, include
from . views import *

urlpatterns = [
    path('kitchenMaster/recipeform/', RecipeView.as_view()),
    path('kitchenMaster/recipeform/one/<str:id>/', OneRecipeView.as_view()),
    path('kitchenMaster/recipeform/fk/<str:fk_id>/', RecipeViewUsingFk.as_view()),
    path('kitchenMaster/recipeform/update/', RecipeUpdate.as_view()),
    path('kitchenMaster/recipeform/add/', RecipeAddView.as_view()),
    path('kitchenMaster/recipeform/<str:id>/', RecipeDeleteView.as_view()),
    path('kitchenMaster/recipeform/search/<str:title>/', SearchRecipe.as_view()),
    path('kitchenMaster/userform/', UserView.as_view()),
    path('kitchenMaster/userform/add/', UserAddView.as_view()),
    path('kitchenMaster/userform/<str:id>/', UserDeleteView.as_view()),
    path('kitchenMaster/finduser/', FindUser.as_view()),
    path('kitchenMaster/findoneuser/<str:email>/', OneUserView.as_view()),
]
