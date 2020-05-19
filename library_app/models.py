from django.db import models
from datetime import datetime

# Create your models here.
#Let's create an application for representing a library. You should have two models (below) and a page for users to check out and check in books. You can enter the book and author information using the admin panel.

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
# Author: a model representing an author of a book, one author can have multiple books


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)

class Book(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)