from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        pass
    context = {
        
    }
    return render(request, 'home/index.html', context)
