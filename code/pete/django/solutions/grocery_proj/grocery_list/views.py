from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required #, user_passes_test
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

from .models import GroceryItem

def super_check(user):
    return user.username.contains('super')

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        GroceryItem.objects.create(
            description=description,
            created_date=timezone.now(),
            user=request.user
        )
        return redirect('grocery_list:index')
        # ^^ this is a shorcut for this:
        # return HttpResponseRedirect(reverse('grocery_list:index'))
    
    groceries = GroceryItem.objects.all()
    completed_groceries = GroceryItem.objects.filter(completed=True)
    incomplete_groceries = GroceryItem.objects.filter(completed=False)


    context = {
        'groceries': groceries,
        'completed_groceries': completed_groceries,
        'incomplete_groceries': incomplete_groceries,
    }
    return render(request, 'grocery_list/index.html', context)

@login_required
def delete(request, id):
    # item = GroceryItem.objects.get(id=id)
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return redirect('grocery_list:index')

@login_required
def complete(request, id):
    # item = GroceryItem.objects.get(id=id)
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return redirect('grocery_list:index')