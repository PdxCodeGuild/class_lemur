from code.swarty.django.lab01.List_Proj.list_app.models import GroceryItem
from django.contrib import admin
from .models import GroceryItem
# Register your models here.
admin.site.register(GroceryItem)