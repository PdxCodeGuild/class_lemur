from django.shortcuts import render, redirect
from django.utils import timezone
from .models import NewUser

def index(request):
    new_user = NewUser.objects.create_user(username=username, password=password)
    
    context = {
        'new_user':
    }
    return render(request, 'Poo_Talk_users/index.html', context)
