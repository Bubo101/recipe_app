from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from meal_plans.models import MealPlan
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


USER_MODEL = settings.AUTH_USER_MODEL

# Create your views here.


class MealPlanListView(LoginRequiredMixin, ListView):
    # if USER_MODEL == MealPlan.owner:
    model = MealPlan
    template_name = "meal_plans/list.html"
    paginate_by = 4
    context_object_name = "meal_plans"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
        # this makes sure only the signed in user has access to the content of the user


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"
    context_object_name = "plan"

    def test_func(self):
        return self.request.user == self.get_object().owner


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "date", "recipes"]

    def get_success_url(self):
        return reverse_lazy("mp_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().owner


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "recipes"]

    def get_success_url(self):
        return reverse_lazy("mp_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().owner


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    context_object_name = "plan"
    success_url = reverse_lazy("meal_plan_list")

    def test_func(self):
        return self.request.user == self.get_object().owner
