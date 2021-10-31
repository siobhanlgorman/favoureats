from django.test import TestCase, Client
from django.urls import reverse
from recipe.models import Recipe, User


class TestViews(TestCase):
    """
    Test views
    """

    def setUp(self):
        """
        Create a test user
        """
        self.client = Client()
        self.user_a = User(username='testuser', email='testuser@email.com')
        self.user_a.set_password('my_password')
        self.client.login(username='testuser', password='my_password')
        self.user_a.save()
        user_b = User.objects.create_user('user_2',
                                          'email@invalid.com',
                                          'a_password')
        self.user_b = user_b

        # create a test recipe
        self.recipe_1 = Recipe.objects.create(
            title='test recipe',
            author=self.user_a,
        )
        self.recipe_detail_url = reverse('recipe_detail', args=['test-recipe'])
        self.recipecreate_url = reverse('recipecreate')

    def test_get_homelist(self):
        """
        Test home page response is 200
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        """
        Test about page response is 200
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_recipes_page(self):
        """
        Test recipes page response is 200
        """
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_access_to_recipe_detail_page_requires_login(self):
        """
        Test logged in user can access recipe detail page
        """
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_edit_recipe_page(self):
        user = self.user_a
        recipe = Recipe.objects.create(title='test recipe 3', author=user)
        response = self.client.get(f'/recipeedit/{recipe.slug}')
