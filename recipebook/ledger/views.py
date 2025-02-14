from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')
# Create your views here.

def task_list(request):
    ctx = {
"tasks": [
"task 1",
"task 2",
"task 3",
"task 4",
"task 5",
    ]
}
    return (HttpResponse(render(request, 'task_list.html', ctx,)))



def recipe_1(request):
    recipe_context = {
    "name": "Recipe 1",
    "ingredients": [
        {
            "name": "tomato",
            "quantity": "3pcs"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "pork",
            "quantity": "1kg"
        },
        {
            "name": "water",
            "quantity": "1L"
        },
        {
            "name": "sinigang mix",
            "quantity": "1 packet"
        }
    ],
    "link": "/recipe/1"
}
    return (HttpResponse(render(request, 'Recipe_template.html', recipe_context,)))

def recipe_2(request):

    recipe_context = {
    "name": "Recipe 2",
    "ingredients": [
        {
            "name": "garlic",
            "quantity": "1 head"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "vinegar",
            "quantity": "1/2cup"
        },
        {
            "name": "water",
            "quantity": "1 cup"
        },
        {
            "name": "salt",
            "quantity": "1 tablespoon"
        },
        {
            "name": "whole black peppers",
            "quantity": "1 tablespoon"
        },
        {
            "name": "pork",
            "quantity": "1 kilo"
        }
    ],
    "link": "/recipe/2"
}
    return (HttpResponse(render(request, 'Recipe_template.html', recipe_context,)))
