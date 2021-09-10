from django.db import models
from django.db.models.base import Model


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.CharField(max_length=50)
    checkout = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book
