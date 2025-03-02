from django.urls import path
from .views import recipe_detail, recipes_lists

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes-lists"),
    path("recipe/<int:id>/", recipe_detail, name="recipe_detail"),
]


# urlpatterns = [
#     path('recipe/1', recipe_1, name = 'recipe_1'),
#     path('recipe/2', recipe_2, name = 'recipe_2'),
#     path('recipes/list', recipe_index, name = 'recipe_index'),
#     path('', recipe_detail, name = 'index'),
# ]

app_name = 'ledger'