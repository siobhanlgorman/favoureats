from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('myrecipes/', views.MyRecipeList.as_view(), name='myrecipes'),
    path('recipecreate/', views.RecipeCreate.as_view(), name='recipecreate'),
    path('recipeedit/<slug:slug>', views.RecipeEdit.as_view(),
         name='recipeedit'),
    path('recipedelete/<slug:slug>', views.RecipeDelete.as_view(),
         name='recipedelete'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('favourite/<slug:slug>', views.RecipeFavourite.as_view(),
         name='recipe_favourite'),
]
