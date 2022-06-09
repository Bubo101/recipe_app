from django.urls import path
from meal_plans.views import (
    MealPlanListView,
    MealPlanDetailView,
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanUpdateView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="mp_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="mp_detail"),
    path("<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mp_delete"),
    path("new/", MealPlanCreateView.as_view(), name="mp_new"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mp_edit"),
]
# lots to edit here
