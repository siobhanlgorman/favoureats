from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_filter = (
        'status', 'created_on', 'type', 'author', 'category')
    list_display = (
        'title', 'author', 'slug', 'status', 'created_on', 'type', 'category')
    search_fields = [
        'title', 'introduction', 'ingredients']
    prepopulated_fields = {
        'slug': ('title',)}
    summernote_fields = (
        'introduction', 'ingredients', 'steps')
