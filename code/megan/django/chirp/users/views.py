from django.shortcuts import render, redirect 
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User 

def log_out(request):

    logout(request)

    return redirect('chirp_app:index')

def log_in(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)


        if user is not None:
            
            login(request, user)

            return redirect('chirp_app:index')
            
    return render(request, 'users/login.html')


def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')

        if password == password_again:
            user = User.objects.create(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('chirp_app:index')

    return render(request, 'users/register.html')
