from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Player
from .forms import PlayerForm

def index(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            messages.success(request, f'{player} has been added')
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
    # messages.warning(request, 'you have been forewarned...')
    return render(request, 'nfl/index.html', context)