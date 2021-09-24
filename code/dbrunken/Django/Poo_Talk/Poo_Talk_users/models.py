from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class NewUser(models.Model):
    new_user_name = User.objects.create_user(username=username, password=password)


    def __str__(self):
        return self.new_user_name
