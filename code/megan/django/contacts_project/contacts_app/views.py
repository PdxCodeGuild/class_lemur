from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        song = request.POST.get('song')
        Contact.objects.create(
            name=name,
            favorite_artist=artist,
            favorite_album=album,
            favorite_song=song
        )
    contacts = Contact.objects.all
    context = {
        'contacts' : contacts
    }
    return render(request, 'contacts_app/index.html', context)
