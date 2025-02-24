from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    Quantity = models.IntegerField(default=1)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name="ingredient")
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
    def __str__(self):
        return self.Ingredient.name