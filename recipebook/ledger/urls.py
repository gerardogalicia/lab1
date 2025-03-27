from django.urls import path
from .views import recipes_lists, view_function, RecipeDetailView, CreateRecipe, CreateRecipeImage

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes_lists"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path('login', view_function, name= 'login'),
    path('add', CreateRecipe.as_view(), name ='add'),
    path('recipe/<int:pk>/add_image', CreateRecipeImage.as_view(), name = 'addimage'),
]

app_name = 'ledger'