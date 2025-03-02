from django.contrib import admin
# Register your models here.
from ledger.models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

    


# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
