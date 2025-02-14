from django.urls import path
from .views import index, task_list, recipe_1, recipe_2, recipe_index

urlpatterns = [
    path('', index, name='index'),
    path('task_list/', task_list, name='task_list'),
    path('Recipe/1', recipe_1, name = 'Recipe_1'),
    path('Recipe/2', recipe_2, name = 'Recipe_2'),
    path('Recipes/', recipe_index, name = 'Recipe_index'),
    ]

app_name = 'ledger'