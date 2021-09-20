from django.contrib import admin

from .models import Chirp, Chirp_comments

admin.site.register(Chirp)
admin.site.register(Chirp_comments)
