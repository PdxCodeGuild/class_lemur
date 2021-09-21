from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User


def get_due_date():
    return date.today() + timedelta(days=20)
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    pubdate=models.DateField()
    genre=models.ManyToManyField('Genre', 'title')
    author=models.ManyToManyField('Author', 'title')
    CHOICES = [(i,str(i)) for i in range(1,11)]
    copies=models.SmallIntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    last_name = models.CharField('Last Name', max_length=40)
    pen_name=models.CharField('Pen Name', max_length=81)
    def __str__(self):
        return self.pen_name

class Tracking(models.Model):
    title = models.ManyToManyField(Book, related_name='state')
    date_out =models.DateField('Date Checkout Out', default=date.today())
    due=models.DateField('Due Date',default= get_due_date)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='patron')
    def __str__(self):
        return f'{self.user}; checked: {self.title}'
class Genre(models.Model):
    name=models.CharField('Genre', max_length=20)
    def __str__(self):
        return self.name

"""
Let's create an application for representing a library. You should have two models (below) 
and a page for users to check out and check in books. You can enter the book and author information using the admin panel.

Book: a model representing a book, with a title, publish date, and an author (foreign key)
Author: a model representing an author of a book, one author can have multiple books
Version 2
Add another model to keep track of who checked out a book and when. When a user checks a 
book back in, record that too. Add a text input on the 'checkout' page to record the name of 
who checked out the book. Have a page to show all the checkouts and returns.

The new model can have the following fields:

book: the book that the user checked out or checked in
user: a text field containing the name of the user that checked out or checked in the book
checkout: a boolean indicating whether the book was checked out or checked in
timestamp: a datetime that records when the book was checked out or in
Optional Version 3
Add a Genre model. Give the Genre model a many-to-many relationship. Each genre can have 
any number of books. Each book can have any number of genres.

Optional Version 4
Add a user authentication system to the project. Instead of a user text field in the 
check out model, make the field a ForeignKey to the User model.
"""