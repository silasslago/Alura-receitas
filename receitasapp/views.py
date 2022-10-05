from django.shortcuts import render

def index(request):

    data_receitas = {
        1: 'Sorvete',
        2: 'Lasanha',
        3: 'Alcachofra'
    }

    data = {
        'receitas': data_receitas
    }

    return render(request, "index.html", data)

def receita(request):
    return render(request, 'receita.html')
