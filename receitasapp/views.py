from django.shortcuts import render

from receitasapp.models import Recipe

def index(request):
    return render(request, "index.html", {
        'receitas': Recipe.objects.values('id', 'name', 'img')
    })

def receita(request, id):
    return render(request, 'receita.html')
