from django.contrib import admin

# Register your models here.

from meal_plans.models import MealPlan


# Register your models here.
class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)
