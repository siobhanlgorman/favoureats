from django.test import TestCase
from .models import Recipe, Review, User


class TestModels(TestCase):

    def setUp(self):

        user_b = User.objects.create_user('user_2', 'email@invalid.com', 'a_password')
        self.user_b = user_b
        self.recipe1 = Recipe.objects.create(
            title='Test Recipe 1',
            author=user_b,
            category='main',
            type='vegetarian'
        )

    def test_recipe_gets_slug_from_title(self):
        self.assertEqual(self.recipe1.slug, 'test-recipe-1')


