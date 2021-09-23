from django.db import models
from django.db.models.base import Model


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='books')
    title = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, related_name='checkouts')
    user = models.CharField(max_length=50)
    checkout = models.BooleanField(default=False)
    time = models.DateTimeField('checkout time', auto_now=True)

    def __str__(self):
        return self.book.title


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.genre
