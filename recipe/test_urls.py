from django.test import SimpleTestCase
from django.urls import reverse, resolve
from recipe.views import HomeList, AboutPage, RecipeList, RecipeDetail, RecipeFavourite, MyRecipeList, RecipeCreate, RecipeEdit, RecipeDelete


class TestUrls(SimpleTestCase):

    def test_homelist_url_is_resolved(self):
        """
        Test redirect to homepage
        """
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeList)

    def test_aboutpage_url_is_resolved(self):
        """
        Test redirect to about page
        """
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, AboutPage)

    def test_recipelist_url_is_resolved(self):
        """
        Test redirect to recipes page
        """
        url = reverse('recipes')
        self.assertEqual(resolve(url).func.view_class, RecipeList)

    def test_recipedetail_url_is_resolved(self):
        """
        Test redirect to recipe detail page
        """
        url = reverse('recipe_detail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeDetail)

    def test_recipefavourite_url_is_resolved(self):
        """
        Test redirect to recipe detail page
        """
        url = reverse('recipe_favourite', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeFavourite)

    def test_myrecipelist_url_is_resolved(self):
        """
        Test redirect to my recipes page
        """
        url = reverse('myrecipes')
        self.assertEqual(resolve(url).func.view_class, MyRecipeList)

    def test_recipe_create_url_is_resolved(self):
        """
        Test redirect to my recipe create page
        """
        url = reverse('recipecreate')
        self.assertEqual(resolve(url).func.view_class, RecipeCreate)

    def test_recipe_edit_url_is_resolved(self):
        """
        Test redirect to recipe edit page
        """
        url = reverse('recipeedit', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeEdit)

    def test_recipe_delete_url_is_resolved(self):
        """
        Test redirect to recipe edit page
        """
        url = reverse('recipedelete', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeDelete)
