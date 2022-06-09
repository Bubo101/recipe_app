from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from meal_plans.models import MealPlan
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    # def get_context_data(self, **kwargs):
    #     # Let the parent class get the context for
    #     # the actual Post for its detail
    #     context = super().get_context_data(**kwargs)

    #     # Get and add your custom data, here
    #     # Just add it to the dictionary
    #     context["views"] = PageVisit.objects.all()[:5]

    #     # return the context for the DetailView
    #     # to return to Django to render the template
    #     from pprint import pprint

    #     pprint(context)
    #     return context


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "date", "recipes"]

    # def test_func(self):
    #     return self.request.user == self.get_object().owner

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mp_detail", pk=plan.id)

    # def get_success_url(self):
    #     return reverse_lazy("mp_detail", kwargs={"pk": self.object.pk})


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "recipes"]

    # def test_func(self):
    #     return self.request.user == self.get_object().owner
    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("mp_detail", pk=plan.id)


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    context_object_name = "plan"
    success_url = reverse_lazy("mp_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
