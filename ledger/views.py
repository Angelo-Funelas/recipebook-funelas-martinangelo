from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "recipes": Recipe.objects.all()
    })

def recipe(request, recipeID):
    return render(request, "recipe.html", {
        "recipe": Recipe.objects.get(id=recipeID),
        "ingredients": RecipeIngredient.objects.filter(Recipe_id=recipeID)
    })