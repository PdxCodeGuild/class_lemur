from django.db import models

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

