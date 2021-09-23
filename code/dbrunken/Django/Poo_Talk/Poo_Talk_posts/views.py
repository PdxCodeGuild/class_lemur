from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import IntegrityError

from .models import Post

def index(request):
       
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'Poo_Talk_posts/index.html', context)

@login_required
def new_post(request):
    if request.method == 'POST':
        post = request.POST.get('post')
        Post.objects.create(
            text=post,
            created_date=timezone.now(),
            created_by=request.user
        )
        return redirect('Poo_Talk_posts:index')

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('Poo_Talk_posts:index')