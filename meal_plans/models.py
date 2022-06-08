from tkinter import CASCADE
from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL
# NEED TO INPUT USER MODEL FROM SETTINGS AND ASSIGN IT TO A VARIABLE BEFORE I CAN USE IT IN FOREIGN KEY

# Create your models here.


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(blank=True)
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")
