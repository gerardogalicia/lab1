from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeImageForm
from django.views.generic import DetailView, CreateView


def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    

class CreateRecipe(CreateView):
    #Thing that allows users to make new recipies
    model = Recipe
    template_name = "ledger/add.html"
    form_class = RecipeForm
    def get_success_url(self):
        return reverse_lazy('ledger:recipes_lists')
    
class CreateRecipeImage(CreateView):
    #Class that allows user to upload images
        model = RecipeImage
        template_name = 'ledger/imageadd.html'
        form_class = RecipeImageForm

        # IT DOES NOT UPDATE!!
             


        def get_success_url(self):
            return reverse_lazy('ledger:recipes_lists')
        

    
        
# Login required view
@login_required
def view_function(request):
    return render(request, "ledger/registration.html")
  



