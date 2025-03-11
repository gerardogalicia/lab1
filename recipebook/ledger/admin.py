from django.contrib import admin
# Register your models here.
from ledger.models import Ingredient, Recipe, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Updated To include author and date fields in list display
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('id', 'name', 'created_on', 'last_updated', 'Author')
    search_fields = ('name',)
    

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)

# unregisters any existing User before reregistering
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
