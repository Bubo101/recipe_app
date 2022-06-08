from django.urls import path
from meal_plans.views import MealPlanListView

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mp_list"),
    # path("<int:pk>/", MealPlanDetailView.as_view(), name="mp_detail"),
    # path("<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mp_delete"),
    # path("new/", RecipeCreateView.as_view(), name="mp_new"),
    # path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="mp_edit"),
    # path("<int:recipe_id>/ratings/", log_rating, name="mp_rating"),
]
# lots to edit here
