from django.test import TestCase, Client
from recipe.models import Recipe



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_homelist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
    
    def test_get_recipes_page(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    # def test_get_recipe_create_page(self):
    #     recipe = Recipe.objects.create(title='test recipe')
    #     response = self.client.get('/recipecreate/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'recipecreate.html')

    # def test_get_recipe_detail_redirects_nonregistered_users(self):
    #     response = self.client.get('self.recipe_detail_url')
    #     self.assertRedirects(response.status_code, 302)
    


