from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "recipes": Recipe.objects.all()
    })

def recipe(request, recipeID):
    recipe = Recipe.objects.get(id=recipeID)
    return render(request, "recipe.html", {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all()
    })