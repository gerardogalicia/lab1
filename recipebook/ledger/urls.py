from django.urls import path
from .views import recipes_lists, view_function, RecipeDetailView

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes_lists"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path('login', view_function, name= 'login')
]

app_name = 'ledger'