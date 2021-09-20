from django.shortcuts import render

from .models import Pokemon

def index(request):
    context = {
        'pokemon': Pokemon.objects.all()
    }
    return render(request, 'pokedex/index.html', context)