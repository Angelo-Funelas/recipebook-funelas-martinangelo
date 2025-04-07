from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

@login_required
def index(request):
    return render(request, 'index.html', {
        'recipes': Recipe.objects.all()
    })

@login_required
def recipe(request, recipeID):
    recipe = Recipe.objects.get(id=recipeID)
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'ingredients': recipe.ingredients.all()
    })
    
@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST['recipe-name']
        ingredient_count = int(request.POST['ingredient-count'])
        recipe = Recipe(name=name, author=request.user.profile)
        recipe.save()
        for i in range(1,ingredient_count+1):
            ingredient_name = request.POST[f'ingredient-{i}-name'].lower()
            ingredient_qty = request.POST[f'ingredient-{i}-qty']
            try:
                ingredient = Ingredient.objects.get(name=ingredient_name)
            except Ingredient.DoesNotExist:
                ingredient = Ingredient(name=ingredient_name)
                ingredient.save()
            recipe_ingredient = RecipeIngredient(ingredient=ingredient, quantity=ingredient_qty, recipe=recipe)
            recipe_ingredient.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'new.html', {
            'ingredients': Ingredient.objects.all()
        })
        
@login_required
def add_image(request, pk):
    if request.method == 'POST':
        image = request.FILES['image']
        description = request.POST['description']
        recipe = Recipe.objects.get(id=pk)
        recipe_image = RecipeImage(image=image, description=description, recipe=recipe)
        recipe_image.save()
        return HttpResponseRedirect(reverse('recipe', kwargs={'recipeID': pk}))