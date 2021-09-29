from django.shortcuts import render, redirect, get_object_or_404

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
        return redirect('/')


    contacts = Contact.objects.all
    context = {
        'contacts' : contacts
    }
    return render(request, 'contacts_app/index.html', context)

def contact(request, id):
    # contact = Contact.objects.get(id=id)
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts_app/contact.html', {'contact': contact})