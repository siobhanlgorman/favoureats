from django.contrib import admin
from django.urls import path, include
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('recipe.urls'), name='recipe_urls'),
    path('accounts/', include('allauth.urls')),

]

handler404 = 'favoureats.views.handler404'
handler500 = 'favoureats.views.handler500'
