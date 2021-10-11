from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def logout_user(request):
    logout(request)
    return redirect('Poo_Talk_posts:index')

def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("user logged in")
            login(request, user)
            return redirect('Poo_Talk_posts:index')

    return render(request, 'Poo_Talk_users/login.html')

def new_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(
                username, password1
            )

            login(request, user)
            return redirect('Poo_Talk_users:login_user')
    
    return render(request, 'Poo_Talk_users/new_user.html')