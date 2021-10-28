"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Recipe(models.Model):
    """
    Model for recipe
    """
    title = models.CharField(
        max_length=200,
        unique=True)
    slug = models.SlugField(
        max_length=200,
        unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipe_posts")
    created_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)
    introduction = models.TextField(
        blank=True,
        )
    ingredients = models.TextField(
        blank=False,
        )
    steps = models.TextField(
        blank=False,
        )
    servings = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(8)])
    cooktime_hours = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(48)])
    cooktime_mins = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(59)])
    recipe_image = CloudinaryField(
        'image',
        default='placeholder')
    status = models.IntegerField(
        choices=STATUS,
        default=0)
    favourites = models.ManyToManyField(
        User,
        related_name='recipe_favourites',
        blank=True)

    BREAKFAST = 'Breakfast'
    STARTER = 'Starter'
    MAIN = 'Main'
    SIDE = 'Side'
    DESSERT = 'Dessert'
    BAKES = 'Bakes'
    SALAD = 'Salad'
    SOUP = 'Soup'

    RECIPE_CATEGORY_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (STARTER, 'Starter'),
        (MAIN, 'Main'),
        (SIDE, 'Side'),
        (DESSERT, 'Dessert'),
        (BAKES, 'Bakes'),
        (SALAD, 'Salad'),
        (SOUP, 'Soup')
    ]

    category = models.CharField(
        max_length=15,
        choices=RECIPE_CATEGORY_CHOICES,
        blank=False,
        default=MAIN
    )

    VEGETARIAN = 'Vegetarian'
    VEGAN = 'Vegan'
    FISH = 'Fish'

    RECIPE_TYPE_CHOICES = [
        (VEGETARIAN, 'Vegetarian'),
        (VEGAN, 'Vegan'),
        (FISH, 'Fish')
    ]

    type = models.CharField(
        max_length=15,
        choices=RECIPE_TYPE_CHOICES,
        default=VEGETARIAN,
        blank=False
    )

    notes = models.TextField(
        blank=True,
        max_length=200)

    class Meta:
        """
        Recipes ordered to show newest first to show regular updates
        """
        ordering = [
            '-created_on']

    def __str__(self):
        return self.title

    def number_of_favourites(self):
        """
        Returns total number of times users have favourited a recipe
        """
        return self.favourites.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class Review(models.Model):
    """
    Model for review. Logged in user can review a recipe
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='reviews')
    name = models.CharField(
        max_length=100)
    email = models.EmailField(
        default=None)
    body = models.TextField(
        blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(
        default=False)

    class Meta:
        """
        Reviews ordered from oldest to newest like a conversation
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
