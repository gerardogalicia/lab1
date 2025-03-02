from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient







def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)


def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe_detail.html', ctx)


















# def recipes_list(request):
#     recipes = Recipe.objects.all() 
#     return render(request, 'recipes_list.html', {'recipes': recipes})
    
   
# def recipe_detail(request):
#     recipe = get_object_or_404(RecipeIngredient)
#     ingredients = RecipeIngredient.ingredientModel 
#     return render(request, 'RecipeIngredient_list.html', {'recipe': recipe, 'ingredients': ingredients})







# # Temp keep this for now. Will erase once finished.
# def recipe_index(request):
#     recipe_context ={
#     "recipes": [
#         {
#             "name": "Recipe 1",
#             "ingredients": [
#                 {
#                     "name": "tomato",
#                     "quantity": "3pcs"
#                 },
#                 {
#                     "name": "onion",
#                     "quantity": "1pc"
#                 },
#                 {
#                     "name": "pork",
#                     "quantity": "1kg"
#                 },
#                 {
#                     "name": "water",
#                     "quantity": "1L"
#                 },
#                 {
#                     "name": "sinigang mix",
#                     "quantity": "1 packet"
#                 }
#             ],
#             "link": "/recipe/1"
#         },
#         {
#             "name": "Recipe 2",
#             "ingredients": [
#                 {
#                     "name": "garlic",
#                     "quantity": "1 head"
#                 },
#                 {
#                     "name": "onion",
#                     "quantity": "1pc"
#                 },
#                 {
#                     "name": "vinegar",
#                     "quantity": "1/2cup"
#                 },
#                 {
#                     "name": "water",
#                     "quanity": "1 cup"
#                 },
#                 {
#                     "name": "salt",
#                     "quantity": "1 tablespoon"
#                 },
#                 {
#                     "name": "whole black peppers",
#                     "quantity": "1 tablespoon"
#                 },
#                 {
#                     "name": "pork",
#                     "quantity": "1 kilo"
#                 }
#             ],
#             "link": "/recipe/2"
#         }
#     ]
# }
#     return (HttpResponse(render(request, 'Recipe_List_Context.html', recipe_context,)))


# def recipe_1(request):
#     recipe_context = {
    
#     "name": "Recipe 1",
#     "ingredients": [
#         {
#             "name": "tomato",
#             "quantity": "3pcs"
#         },
#         {
#             "name": "onion",
#             "quantity": "1pc"
#         },
#         {
#             "name": "pork",
#             "quantity": "1kg"
#         },
#         {
#             "name": "water",
#             "quantity": "1L"
#         },
#         {
#             "name": "sinigang mix",
#             "quantity": "1 packet"
#         }
#     ],
#     "link": "/recipe/1"
# }
#     return (HttpResponse(render(request, 'Recipe_template.html', recipe_context,)))

# def recipe_2(request):

#     recipe_context = {
#     "name": "Recipe 2",
#     "ingredients": [
#         {
#             "name": "garlic",
#             "quantity": "1 head"
#         },
#         {
#             "name": "onion",
#             "quantity": "1pc"
#         },
#         {
#             "name": "vinegar",
#             "quantity": "1/2cup"
#         },
#         {
#             "name": "water",
#             "quantity": "1 cup"
#         },
#         {
#             "name": "salt",
#             "quantity": "1 tablespoon"
#         },
#         {
#             "name": "whole black peppers",
#             "quantity": "1 tablespoon"
#         },
#         {
#             "name": "pork",
#             "quantity": "1 kilo"
#         }
#     ],
#     "link": "/recipe/2"
# }
#     return (HttpResponse(render(request, 'Recipe_template.html', recipe_context,)))
