from django.urls import path
from .views import recipe_detail, recipes_lists, view_function

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes_lists"),
    path("recipe/<int:id>/", recipe_detail, name="recipe_detail"),
    path('login', view_function, name= 'login')
]

app_name = 'ledger'