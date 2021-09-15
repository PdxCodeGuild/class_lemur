from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta




def get_due_date():
    return datetime.today() + timedelta(days=20)
# Create your models here.
class Book(models.Model):
    title = models.CharField('Title', max_length=40)
    publisher = models.CharField('Publisher', max_length=40)
    pubdate=models.DateField('Date Published')
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    last_name = models.CharField('Last Name', max_length=40)
    works=models.ManyToManyField(Book, related_name='authors')
    pen_name=models.CharField('Pen Name', max_length=60)
    def __str__(self):
        return self.first_name+ ' ' +self.last_name

class Tracking(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    last_name = models.CharField('Last Name', max_length=40)
    book = models.ManyToManyField(Book, related_name='state')
    date_out =models.DateField('Date Checkout Out', default=datetime.today())
    due=models.DateField('Due Date',default= get_due_date)

class Genre(models.Model):
    genre=models.ManyToManyField(Author, related_name='genre' ,max_length=40)

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