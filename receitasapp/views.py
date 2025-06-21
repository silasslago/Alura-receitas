from http.client import HTTPResponse

from django.shortcuts import render

from receitasapp.forms import SearchForm
from receitasapp.models import Recipe, RecipeCategory


def index(request):
    recipies = None
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data["search"]
            category_id = form.cleaned_data["category_id"]
            print(category_id)
            if(category_id != None):
                recipies = Recipe.objects.filter(category=category_id)
            else:
                recipies = Recipe.objects.filter(name__contains=name)
        else:
            raise Exception("O formulário não é válido.")
    else:
        recipies = Recipe.objects.values('id', 'name', 'img')

    return render(request, "index.html", {
        'receitas': recipies
    })

def receita(request, id):
    recipe = Recipe.objects.filter(id=id).first()
    recipe_categories = RecipeCategory.objects.all()
    return render(request, 'receita.html', {
        'recipe': recipe,
        'categories': recipe_categories,
    })
