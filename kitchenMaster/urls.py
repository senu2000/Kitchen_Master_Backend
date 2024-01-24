from django.urls import path, include
from rest_framework import routers
from kitchenMaster import views

router = routers.DefaultRouter()
router.register(r'userform', views.UserView, basename='kitchenMaster')
router.register(r'recipeform', views.RecipeView, basename='kitchenMaster')

urlpatterns = [
    path('kitchenMaster/', include(router.urls)),
]
