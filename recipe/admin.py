from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Recipe)
# @admin.register(Recipe)
# class RecipeAdmin(SummernoteModelAdmin):
#     summernote_fields = ('introduction', 'ingredients', 'steps')
