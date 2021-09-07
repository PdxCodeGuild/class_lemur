from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context= {'colors': ['red', 'green', 'blue'],}
    return render(request, 'demo_app/index.html', context)