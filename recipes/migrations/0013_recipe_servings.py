# Generated by Django 4.0.3 on 2022-06-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_alter_shoppingitem_food_item_alter_shoppingitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
