from django.contrib import admin

from .models import Doggo, Owner

admin.site.register(Doggo)
admin.site.register(Owner)