from django.shortcuts import get_object_or_404, render, redirect
from .models import GroceryItem


def index(request):
    if request.method == 'POST':
        if 'add-item' in request.POST:
            print(request.POST)
            item = request.POST.get('item')
            completed = request.POST.get('completed')
            created_date = request.POST.get('created_date')
            completed_date = request.POST.get('completed_date')
            GroceryItem.objects.create(
                item=item,
                completed=completed,
                created_date=created_date,
                completed_date=completed_date
            )
        elif 'update' in request.POST:
            items = GroceryItem.objects.filter(completed=True)
            items_incomplete = GroceryItem.objects.filter(completed=False)

            for item in items_incomplete:
                complete = request.POST.get(f'{item}completed-check')
                delete = request.POST.get(f'{item}delete-check')
                if complete:
                    item.completed = True
                    item.save()
                if delete:
                    item.delete()

            for item in items:
                complete = request.POST.get(f'{item}completed-check')
                delete = request.POST.get(f'{item}delete-check')
                if not complete:
                    item.completed = False
                    item.completed_date = ''
                    item.save()
                if delete:
                    item.delete()

        return redirect('/')

    items = GroceryItem.objects.all()

    context = {
        'items': items,
    }
    return render(request, 'lab01_app/index.html', context)
