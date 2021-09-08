from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world, you're at the polls index.")