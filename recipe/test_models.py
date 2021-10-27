from django.test import TestCase
from .models import Recipe, Review, User


class TestModels(TestCase):

    def setUp(self):
        user_a = User.objects.create_user('user_1',
                                          'testuser@email.com',
                                          'my_password')
        self.user_a = user_a
        user_b = User.objects.create_user('user_2',
                                          'email@valid.com',
                                          'a_password')
        self.user_b = user_b
        self.recipe1 = Recipe.objects.create(
            title='Test Recipe 1',
            author=user_b,
            category='main',
            type='vegetarian'
        )

    def test_recipe_gets_slug_from_title(self):
        """
        Tests that slug is automatically generated from recipe title
        """
        self.assertEqual(self.recipe1.slug, 'test-recipe-1')

    def test_model_title_output_is_string(self):
        """
        Tests that title is a string
        """
        self.assertEqual(str(self.recipe1.title), 'Test Recipe 1')

    def test_recipe_favourites_users(self):
        """
        Tests that total number of favourites is counted
        """
        testuser = User.objects.create_user(
            username='testuser1', password='my_password')

        testuser2 = User.objects.create_user(
            username='testuser2', password='my_other_password')

        title = Recipe.objects.create(
            title='Soup', author=testuser)

        title.favourites.set([testuser.pk, testuser2.pk])
        self.assertEqual(title.favourites.count(), 2)
