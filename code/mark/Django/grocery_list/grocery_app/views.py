from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import GroceryItem
# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'description' in request.POST:
            description = request.POST.get("description")
            complete = False  
            GroceryItem.objects.create(description=description, complete=complete)
            return redirect('/#the_list')
        elif 'delete' in request.POST:
            id = request.POST.get('delete')
            GroceryItem.objects.filter(id=id).delete()
            return redirect('/#the_list')
        else:
            id = request.POST.get('id')
            grocery_item = get_object_or_404(GroceryItem, pk=id)
            grocery_item.complete = not grocery_item.complete
            if grocery_item.complete == False:
                grocery_item.complete_date = None
            else:
                grocery_item.complete_date = timezone.now()
            grocery_item.save()
            return redirect('/#the_list')
    grocery_items = GroceryItem.objects.all()
    context = {
        'grocery_items': grocery_items 
    }
    return render(request, 'grocery_app/index.html', context)


