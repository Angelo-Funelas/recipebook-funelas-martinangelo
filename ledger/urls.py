from django.urls import path
from . import views

urlpatterns = [
    path("list", views.index, name="index"),
    path("<int:recipe_index>", views.recipe, name="recipe")
]