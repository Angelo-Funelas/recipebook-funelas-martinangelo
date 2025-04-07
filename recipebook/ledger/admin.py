from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Profile, Recipe, Ingredient, RecipeIngredient, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('ingredient', 'recipe', 'quantity',)
    list_filter = ('recipe', 'ingredient',)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0
    
class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    inlines = [RecipeIngredientInline, RecipeImageInline]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)