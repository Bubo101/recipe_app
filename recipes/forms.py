from django import forms


from recipes.models import Rating, Recipe


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]


# class ServingForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ["servings"]
