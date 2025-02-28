from django.contrib import admin

# Register your models here.
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

# class RecipeIngredientAdmin(admin.ModelAdmin):
#     model = RecipeIngredient

# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

# SITE LOGIN INFO DELETE ONCE DONE
# USER: admin
# Password: admin