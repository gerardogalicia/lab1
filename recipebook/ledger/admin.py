from django.contrib import admin
# Register your models here.
from ledger.models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class RecipeInLine (admin.TabularInline):
    model = RecipeIngredient

class ImageInline(admin.StackedInline):
    #Inline for Recipe Images
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    #Class that manages Recipe deteils
    model = Recipe
    inlines = [RecipeInLine, ImageInline]    

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

# unregisters any existing User before reregistering
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
