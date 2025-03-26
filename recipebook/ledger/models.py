from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    bio = models.TextField(blank=True) # Max Length is supposed to be over 255 chars according to specs

    def __str__(self):
        return self.author

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.pk)])
    

    # Gets made only once, when the model is created
    created_on = models.DateTimeField(auto_now_add=True)

    # Refreshes with any changes made.
    last_updated = models.DateTimeField(auto_now=True)
    
    Author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='profile_name')


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
        
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='recipe',
        )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, 
        related_name='ingredients',
    )




# Create a RecipeImage model, which has the following fields:
# Image, that should not be allowed to be empty
# Description that is no more than 255 characters long
# Foreign Key to the Recipe model, with an appropriate related_name attribute

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', default=None)
    description = models.CharField(max_length=255, null=True)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recipe'
    )
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, default=None)