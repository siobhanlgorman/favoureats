from django.test import TestCase, Client
from django.urls import reverse
from recipe.models import Recipe, Review


class TestViews(TestCase):

    def test_recipe_list_GET(self):
        client = Client()

        response = client.get(reverse('recipes'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')
