from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list", views.index, name="index"),
    path("recipe/<int:recipe_index>", views.recipe, name="recipe")
]