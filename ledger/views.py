from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def recipe(request, recipe_index):
    return render(request, "recipe.html")