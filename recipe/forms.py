from django import forms
from .models import Review, Recipe


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'steps', 'servings', 'cooktime_hours', 'cooktime_mins', 'recipe_image')
