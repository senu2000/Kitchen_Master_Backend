from django.urls import path, include
from . views import *

urlpatterns = [
    path('kitchenMaster/recipeform/', RecipeView.as_view()),
    path('kitchenMaster/recipeform/update/', RecipeUpdate.as_view()),
    path('kitchenMaster/recipeform/<str:id>/', RecipeDeleteView.as_view()),
    path('kitchenMaster/userform/', UserView.as_view()),
    path('kitchenMaster/userform/add/', UserAddView.as_view()),
    path('kitchenMaster/userform/<str:id>/', UserDeleteView.as_view()),
]
