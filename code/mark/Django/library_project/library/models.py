from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Checkout(models.Model):
    book_title = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='book')
    image = models.URLField()
    checked_out = models.BooleanField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
