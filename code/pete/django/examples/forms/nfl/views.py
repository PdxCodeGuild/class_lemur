from django.shortcuts import render, redirect

from .models import Player
from .forms import PlayerForm

def index(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    players = Player.objects.all()
    form = PlayerForm()
    context = {
        'players': players,
        'form': form
    }
    # context = { # shorter version of the above lines
    #     'players': Player.objects.all()
    #     'form': PlayerForm()
    # }
    return render(request, 'nfl/index.html', context)