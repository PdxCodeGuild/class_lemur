from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from posts_app.forms import PostForm
from posts_app.models import Post

# Create your views here.
def dashboard(request):
    form = PostForm()
    posts = Post.objects.all()
    context = {
        'form':form,
        'posts':posts, 
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return render(request, 'users_app/dashboard.html', context)
    return render(request, 'users_app/dashboard.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect(reverse('users_app:dashboard'))
    elif request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'users_app/register.html', context)
