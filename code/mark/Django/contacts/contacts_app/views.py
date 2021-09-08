from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        favorite_fruit = request.POST.get("favorite_fruit")
        favorite_color = request.POST.get("favorite_color")
        Contact.objects.create(
            name=name,
            favorite_fruit=favorite_fruit,
            favorite_color=favorite_color
        )
        return redirect('/')
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts_app/index.html', context)