from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts_app/feed.html', context)

def post(request):
    form = PostForm()
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'posts_app/post.html', context)
    return render(request, 'posts_app/post.html', context)