from django.contrib import admin
# Register your models here.
from ledger.models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('id', 'name')
    search_fields = ('name',)
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
