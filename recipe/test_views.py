from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from recipe.models import Recipe, User

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # self.user = User.objects.create_user(username='testuser', password='my_password')
        # self.login = self.client.login(username='testuser', password='my_password')
        # self.recipe_1 = Recipe.objects.create(
        # )
     
        # create a test user
        self.user_a = User(username='testuser', email='testuser@email.com')
        self.user_a.set_password('my_password')
        self.client.login(username='testuser', password='my_password')
        self.user_a.save()

        # create a test recipe
        self.recipe_1 = Recipe.objects.create(
            title='test recipe',
            author=self.user_a,
        )
        self.recipe_detail_url = reverse('recipe_detail', args=['test-recipe'])

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_recipe_count(self):
        recipe_count = Recipe.objects.all().count()
        self.assertEqual(recipe_count, 1)

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

    def test_logged_in_user_can_access_recipe_detail_page(self):
        """
        Test logged in user can access recipe detail page
        """
        user = self.user_a
        recipe = self.recipe_1
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.recipe_1.slug, 'test-recipe')
    
    def test_logged_in_user_can_access_recipe_create_page(self):
        """
        Test logged in user can access recipe detail page
        """
        user = self.user_a
        recipe = self.recipe_1
        response = self.client.get(self.recipe_create_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.recipe_1.slug, 'test-recipe')
    
 


    # def test_get_recipe_create_page(self):
    #     """
    #     Test logged in user can access recipe create and page response is 200
    #     """
    #     recipe = 'test recipe'
    #     user = self.user_a
    #     response = self.client.get('/recipecreate/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'recipecreate.html')


    # def test_user_can_submit_recipe_create_form

    # def test_user_can_delete_recipe

    # def test_get_recipe_detail_redirects_nonregistered_users(self):
    #     response = self.client.get('self.recipe_detail_url')
    #     self.assertRedirects(response.status_code, 302)



    # def test_get_recipe_edit_page(self)
    # def test_get_recipe_delete_page(self)
    


