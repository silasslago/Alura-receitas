from django.contrib import admin
from receitasapp.models import Recipe
from receitasapp.models import RecipeCategory

admin.site.register(Recipe)
admin.site.register(RecipeCategory)