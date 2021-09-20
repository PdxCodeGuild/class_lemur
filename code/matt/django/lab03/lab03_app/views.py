from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Chirp, Chirp_comments


def index(request):
    chirps = Chirp.objects.order_by('-created_at')
    context = {
        'chirps': chirps,
    }
    return render(request, 'lab03_app/index.html', context)


@login_required
def chirp(request):
    if request.method == 'POST':
        chirp = request.POST.get('chirp')
        Chirp.objects.create(
            chirp=chirp,
            user=request.user
        )

        return redirect('lab03_app:index')

    return render(request, 'lab03_app/index.html')


@login_required
def chirp_comments(request, id):
    if request.method == 'POST':
        comment = request.POST.get('reply')
        Chirp_comments.objects.create(
            comment=comment,
            user=request.user
        )
    chirp = get_object_or_404(Chirp, id=id)
    context = {
        'chirp': chirp,
    }
    return render(request, 'lab03_app/chirp.html', context)


@login_required
def likes(request, id):
    like = get_object_or_404(Chirp, id=id)
    like.likes.add(request.user)
    return redirect('lab03_app:index')


@login_required
def delete(request, id):
    chirp = get_object_or_404(Chirp, id=id)
    chirp.delete()
    return redirect('lab03_app:index')
