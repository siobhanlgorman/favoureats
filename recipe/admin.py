from django.contrib import admin
from .models import Recipe, Review
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
        'introduction', 'ingredients', 'steps', 'notes')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
