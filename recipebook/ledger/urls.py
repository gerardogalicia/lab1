from django.urls import path
from .views import recipe_1, recipe_2, recipe_index

urlpatterns = [
    path('recipe/1', recipe_1, name = 'recipe_1'),
    path('recipe/2', recipe_2, name = 'recipe_2'),
    path('recipes/list', recipe_index, name = 'recipe_index'),
    ]

app_name = 'ledger'