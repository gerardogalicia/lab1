from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView


def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)

# def recipe_detail(request, id):
#     ctx = {'recipe': Recipe.objects.get(id=id)}
#     return render(request, 'ledger/recipe_detail.html', ctx)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    




# Login required view
@login_required
def view_function(request):
    return render(request, "ledger/registration.html")
  



