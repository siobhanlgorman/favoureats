from django.test import TestCase
from .models import Recipe, Review, User


# class TestModels(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='john@email.com', password='12345')
#         login = self.client.login(username='testuser', password='12345')
#         # self.user = User.objects.create_user(username='john', email='john@email.com', password='top_secret')
#         self.recipe1 = Recipe.objects.create(
#             title='Recipe1',
#             Author='testuser'
#         )

#     def test_recipe_is_slugified_on_creation(self):
#         self.assertEqual(self.recipe1.slug, 'Recipe-1')


    # def test_recipe_defaults_to_draft(self):
    #     recipe = Recipe.objects.create(title='Test Recipe')
    #     self.assertFalse(item.done)
