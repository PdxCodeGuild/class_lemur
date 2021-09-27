from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Chirp(models.Model):
    text = models.TextField(max_length=140)
    name = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))   

    def __str__(self):
        return self.text
