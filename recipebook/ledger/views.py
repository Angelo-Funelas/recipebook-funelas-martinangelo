from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html", {
        "recipes": Recipe.objects.all()
    })

@login_required
def recipe(request, recipeID):
    recipe = Recipe.objects.get(id=recipeID)
    return render(request, "recipe.html", {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all()
    })