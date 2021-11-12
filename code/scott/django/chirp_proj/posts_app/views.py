from django.shortcuts import render
from .models import Post

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts_app/feed.html', context)