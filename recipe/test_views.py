from django.test import TestCase, Client
from django.urls import reverse
from recipe.models import Recipe, Review


class TestViews(TestCase):
    
    # def setUp(self):
    #     self.client = Client()
    #     self.author = Recipe.objects.create_author('john', 'john@email.com', 'black123#')
    #     # self.client.login(username='john', password='johnpassword')


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

    # def test_get_recipe_detail(self):
    #     response = self.client.get('/recipe_detail/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'recipe_detail.html')

    # def test_about_page_GET
    # def test_myrecipes_page_GET

    # def test_create_recipe_page(self):
    #     recipe = Recipe.objects.create(title='Test Recipe')
    #     response = self.client.get(f'/recipecreate/{recipe.slug}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, '/recipecreate.html')


    # def test_edit_item
    # def test_delete_item


