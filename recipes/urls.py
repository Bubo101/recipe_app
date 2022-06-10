from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipeListView,
    ShoppingListView,
    create_shopping_item,
    delete_shopping_list,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("shopping_items/", ShoppingListView.as_view(), name="shopping_list"),
    path(
        "shopping_items/create/<int:pk>/<int:recipe_id>/",
        create_shopping_item,
        name="create_shopping",
    ),
    path(
        "shopping_items/delete/", delete_shopping_list, name="delete_shopping"
    ),
]
