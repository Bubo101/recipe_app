from ast import Delete
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from meal_plans.models import USER_MODEL
from recipes.forms import RatingForm


from recipes.models import FoodItem, Recipe, ShoppingItem


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)
    # wrote try/except to fix error of internal page not
    # found when deleted while someone is rating it
    # redirects back to home


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()

        food_list = []

        for item in self.request.user.shopping_items.all():
            food_list.append(item.food_item)

        context["food_list"] = food_list

        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")
    # need save_m2m method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "author", "description", "image"]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "recipes/shoppinglist.html"
    context_object_name = "shopping_lists"

    def get_queryset(self):
        return ShoppingItem.objects.filter(user=self.request.user)


# need to use user as the field to start the filter because it is in the model


def create_shopping_item(request, pk, recipe_id):
    if request.method == "POST":
        item = ShoppingItem(
            user=request.user, food_item=FoodItem.objects.get(pk=pk)
        )
        item.save()
        return redirect("recipe_detail", pk=recipe_id)
    else:
        return redirect("recipes_list")


def delete_shopping_list(request):
    if request.method == "POST":
        user_items = ShoppingItem.objects.filter(user=request.user)
        user_items.delete()
        return redirect("shopping_list")
