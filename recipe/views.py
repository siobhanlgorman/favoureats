from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Recipe
from .forms import ReviewForm
from django.urls import reverse_lazy


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
        favourited = False
        if recipe.favourites.filter(id=self.request.user.id).exists():
            favourited = True

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "reviews": reviews,
                "reviewed": False,
                "favourited": favourited,
                "review_form": ReviewForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.filter(approved=True).order_by('-created_on')
        # check if logged in user has liked this recipe
        favourited = False
        if recipe.favourites.filter(id=self.request.user.id).exists():
            favourited = True

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.recipe = recipe
            review.save()
            messages.success(request, 'Thanks for reviewing this recipe!')
        else:
            review_form = ReviewForm()

        return render(
            request,
            'recipe_detail.html',
            {
                "recipe": recipe,
                "reviews": reviews,
                "reviewed": True,
                "favourited": favourited,
                "review_form": ReviewForm()

            },
        )


class RecipeFavourite(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

class MyRecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'myrecipes.html'
    paginate_by = 6


class RecipeCreate(generic.CreateView):
    model = Recipe
    fields = ['author', 'slug', 'recipe_image', 'title', 'ingredients', 'steps', 'servings', 'cooktime_hours', 'cooktime_mins', 'type', 'category', ]
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('myrecipes')
