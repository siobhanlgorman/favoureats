from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class HomeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[0:3]
    template_name = 'index.html'


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.filter(approved=True).order_by('created_on')
        # check if logged in user has liked this recipe
        favourites = False
        if recipe.favourites.filter(id=self.request.user.id).exists():
            favourites = True

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "reviews": reviews,        
                "favourites": favourites,

            },
        )
