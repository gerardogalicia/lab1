from django.db import models
from django.urls import reverse



# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])

# RecipeIngredient needs to have a quantity and an ingredient field 
# that is a foreign key to the Ingredient model and a recipe field 
# that is a foreign key to the Recipe model

class RecipeIngredient(models.Model):

    ingredientModel = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        null=True,
        related_name="Ingredient",
        )
    
    recipeModel = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, 
        null=True,
        related_name="Recipe",
    )