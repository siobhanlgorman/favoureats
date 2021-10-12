from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes')
]
