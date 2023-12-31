# Generated by Django 4.0.3 on 2022-06-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_recipe_author'),
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='recipes',
            field=models.ManyToManyField(related_name='meal_plans', to='recipes.recipe'),
        ),
    ]
