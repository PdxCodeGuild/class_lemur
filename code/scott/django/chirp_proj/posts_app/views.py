from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'hi':'Hello',
    }
    return render(request, 'posts_app/index.html', context)