from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Review


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin panel
    """
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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Add fields for additional display in admin panel
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
