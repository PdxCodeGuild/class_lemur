from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import redirect, render


# Create your views here.
def dashboard(request):
    return render(request, 'users_app/dashboard.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect(reverse('users_app:dashboard'))
    else:
        form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'users_app/register.html', context)
