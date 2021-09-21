from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import User_Info
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_one = request.POST.get('password1')
        password_two = request.POST.get('password2')

        if password_one == password_two:
            user = User.objects.create_user(
                password = password_one,
                username = username 
            )
            User_Info.objects.create(user_name = username)
            return redirect('posts:index')
        else:
            return redirect('posts:home')
            
    return render(request, 'users/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('posts:index')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('posts:index')
