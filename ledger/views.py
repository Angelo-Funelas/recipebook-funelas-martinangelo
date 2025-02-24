from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "recipes": Recipe.objects.all()
    })

def recipe(request, recipe_index):
    return render(request, "recipe.html", {
        "recipe": Recipe.objects.get(id=recipe_index),
        "ingredients": RecipeIngredient.objects.filter(Recipe_id=recipe_index)
    })