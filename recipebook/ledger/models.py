from django.db import models




# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

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
        related_name="recipe",
    )