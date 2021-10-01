from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import user_posts

# Create your views here.
def index(request):
    if request.method == 'POST':
        text = request.POST.get("text")
        print(request.POST)
        user_posts.objects.create(
            user=request.user,
            text=text,
            created_date = timezone.now()
        )
        # return redirect('posts:index')
    
    posts = user_posts.objects.all().order_by('-created_date')
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)

def user_profile(request, id):
    user = User.objects.get(id=id)
    posts = user_posts.objects.all().order_by('-created_date')
    this_user = user.username
    current_user_posts = user_posts.objects.filter(user = user.id)
    context = {
        'user' : user,
        'posts' : posts,
        'current_user' : current_user_posts,
        'this_user' : this_user
    }
    return render(request, 'posts/user_profile.html', context)

