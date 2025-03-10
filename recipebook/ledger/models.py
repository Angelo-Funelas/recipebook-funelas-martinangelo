from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255, null=True)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes")
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("recipe", kwargs={"recipeID": self.id})
    
class RecipeIngredient(models.Model):
    Quantity = models.IntegerField(default=1)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name="recipe_ingredients")
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    def __str__(self):
        return self.Ingredient.name