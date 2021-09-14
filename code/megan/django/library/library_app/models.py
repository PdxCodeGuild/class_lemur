from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author')
    checked_out = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name



class Checked(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book')
    user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='user')
    checkout = models.BooleanField(default=False)
    out_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.name
        

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name