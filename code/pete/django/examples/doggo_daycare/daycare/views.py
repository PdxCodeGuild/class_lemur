from django.shortcuts import redirect, render, get_object_or_404

from random import choice

from .models import Doggo, Owner

def index(request):
    breeds = ['Husky', 'Chihuahua', 'Dalmation']
    doggos = Doggo.objects.all()
    print()
    print('doggos')
    print(doggos)
    print()
    context = {
        'breed': choice(breeds),
        'doggos': doggos,
    }
    return render(request, 'daycare/index.html', context)

def drop_off(request):
    if request.method == 'POST':
        print(request.POST)

        owner_id = int(request.POST.get('owner'))
        owner = Owner.objects.get(id=owner_id)

        name = request.POST.get('name')
        breed = request.POST.get('breed')
        weight = request.POST.get('weight')
        temperament = request.POST.get('temperament')
        bio = request.POST.get('bio')
        photo = request.POST.get('photo')

        Doggo.objects.create(
            owner=owner,
            name=name,
            breed=breed,
            weight=weight,
            temperament=temperament,
            bio=bio,
            photo=photo
        )

        return redirect('/')

    breeds = ['Husky', 'Chihuahua', 'Dalmation']
    owners = Owner.objects.all()
    temperaments = [
        'aggresive',
        'lazy',
        'shy',
        'nervous',
        'psycho',
        'friendly',
    ]
    context = {
        'breed': choice(breeds),
        'owners': owners,
        'temperaments': temperaments,
    }
    return render(request, 'daycare/drop_off.html', context)

def owner_profile(request, id):
    owner = get_object_or_404(Owner, id=id)
    return render(request, 'daycare/owner_profile.html', {'owner': owner})