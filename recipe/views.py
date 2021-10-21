from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from .models import Recipe
from .forms import ReviewForm


class HomeList(generic.ListView):
    """
    Displays three most recent recipes on landing page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[0:3]
    template_name = 'index.html'


class RecipeList(generic.ListView):
    """
    Displays summary view of all recipes with 6 to a page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class AboutPage(generic.TemplateView):
    """
    Displays information about the site
    """
    template_name = 'about.html'


class RecipeDetail(LoginRequiredMixin, View):
    """
    Displays full recipe to logged in users.
    Logged in user can favourite/unfavourite a recipe and leave a review
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Gets full published recipe with approved comments and checks if recipe has been favourited by current user
        User can favourite/unfavourite recipe
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.filter(approved=True).order_by('created_on')
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
        """
        Gets full published recipe with approved comments and checks if recipe has been favourited by current user
        User can submit a review form for approval by admin
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.filter(approved=True).order_by('-created_on')
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


class RecipeFavourite(LoginRequiredMixin, View):
    """
    Logged in user can favourite/unfavourite a recipe
    """

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class MyRecipeList(LoginRequiredMixin, generic.ListView):
    """
    Displays logged in user's own recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'myrecipes.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        """
        Filters recipe list by name of currently logged in user
        User can search recipes by title
        """
        context = super().get_context_data(**kwargs)
        context['recipe'] = context['recipe'].filter(author=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['recipe'] = context['recipe'].filter(
                title__icontains=search_input
            )
        context['search_input'] = search_input

        return context


class RecipeCreate(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    """
    Logged in user can create a recipe and add to my recipes list
    """
    model = Recipe
    fields = ['recipe_image', 'title', 'introduction', 'ingredients', 'steps', 'servings', 'cooktime_hours', 'cooktime_mins', 'type', 'category', 'notes', ]
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('myrecipes')
    success_message = "You have added a recipe to your list!"


    def form_valid(self, form):
        """
        Sets logged in user as author field in form
        Sets form default status to published
        """
        form.instance.author = self.request.user
        form.instance.status = 1
        return super(RecipeCreate, self).form_valid(form)
        


class RecipeEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Logged in user can edit a recipe from their my recipes list
    """
    model = Recipe
    fields = ['author', 'slug', 'recipe_image', 'title', 'introduction', 'ingredients', 'steps', 'servings', 'cooktime_hours', 'cooktime_mins', 'type', 'category', 'notes', ]
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('myrecipes')
    success_message = "You have updated your recipe!"


class RecipeDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    Logged in user can delete a recipe from their my recipes list
    """
    model = Recipe
    success_url = reverse_lazy('myrecipes')
    success_message = "Recipe deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(RecipeDelete, self).delete(request, *args, **kwargs)

