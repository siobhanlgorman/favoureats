from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Review

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_a = User(username='testuser')
        self.user_a.set_password('top_secret')
        self.client.login(username='testuser', password='top_secret')
        self.user_a.save()
        self.recipe_1 = Recipe.objects.create(author=self.user_a, title='test recipe')
        # self.recipes_url = reverse('recipes')
        self.recipe_detail_url = reverse('recipe_detail', args=['test-recipe'])
        # self.post_delete_url = reverse('post_delete', args=['test-post'])
        # self.profiles_url = reverse('profile')
        # self.profile_detail_url = reverse('profile_detail', args=['user_a'])

    #     self.author = Recipe.objects.create_author('john', 'john@email.com', 'black123#')
    #     # self.client.login(username='john', password='johnpassword')
    #       def setUp(self):
    #     self.client = CLient()
    #     self.user = User.objects.create_user(username='testuser', email='john@email.com', password='12345')
    #     login = self.client.login(username='testuser', password='12345')
    #     self.recipe1 = Recipe.objects.create(
    #         title='Recipe1',
    #         User='testuser'
    #         )

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_recipe_list(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_get_recipe_detail(self):
        print('test_get_recipe_detail')
        user = self.user_a
        recipe = self.recipe_1
        response = self.client.get('/recipe_detail/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    # def test_about_page_GET
    # def test_myrecipes_page_GET

    # def test_create_recipe_page(self):
    #     recipe = Recipe.objects.create(title='Test Recipe')
    #     response = self.client.get(f'/recipecreate/{recipe.slug}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, '/recipecreate.html')


    # def test_edit_item
    # def test_delete_item