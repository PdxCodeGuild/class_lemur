from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import Chirp
from .forms import ChirpForm

def super_check(user):
    return user.username.contains('super')

def index(request): 

    if request.method == 'POST':
            
        form = ChirpForm(request.POST)

        if form.is_valid():

            form.save()

        return redirect('chirp_app:index')

    chirps = Chirp.objects.order_by('-date')
    form = ChirpForm()

    context = {
        'chirps': chirps,
        'form': form,
    }

    return render(request, 'chirp_app/index.html', context)

def profile(request):

    chirps = Chirp.objects.all()

    context = {
        'chirps': chirps,
    }

    return render(request, 'chirp_app/profile.html', context)