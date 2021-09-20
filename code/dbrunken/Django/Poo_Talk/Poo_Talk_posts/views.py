from django.shortcuts import render
from django.shortcuts import HttpResponse

def posts(request):
    return HttpResponse('poo posts')