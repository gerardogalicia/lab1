from django.urls import path
from .views import index, task_list, recipe_1, recipe_2

urlpatterns = [
    path('', index, name='index'),
    path('task_list/', task_list, name='task_list'),
    path('Recipe_1/', recipe_1, name = 'Recipe_1'),
    path('Recipe_2/', recipe_2, name = 'Recipe_2'),
    
    ]

app_name = 'ledger'