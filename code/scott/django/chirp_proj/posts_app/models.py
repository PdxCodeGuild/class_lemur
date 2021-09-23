from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=128)
    poster = models.ForeignKey(User, on_delete=models.PROTECT)