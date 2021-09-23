from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User


def register_user(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password')
    password2 = request.POST.get('confirm-password')

    if password1 == password2:
        user = User.objects.create_user(
            username=username,
            password=password1
        )
        login(request, user)
        return redirect('lab03_app:index')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lab03_app:index')


def logout_user(request):
    logout(request)
    return redirect('lab03_app:index')
