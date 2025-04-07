from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list/", views.index, name="index"),
    path("recipe/<int:recipeID>/", views.recipe, name="recipe"),
    path("recipe/add/", views.add, name="add"),
    path("recipe/<int:pk>/add_image/", views.add_image, name="add_image"),
]