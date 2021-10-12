from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeList.as_view(), name='home')
]
