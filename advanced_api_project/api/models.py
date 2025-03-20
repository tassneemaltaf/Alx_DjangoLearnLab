from django.db import models

#Author model with name as an attribute
class Author(models.Model):
  name = models.CharField(max_length=255)

#Book model, with title, publication_year and author as attributes. Author is a foreign key to the Atuhor model, one to many relationship.
class Book(models.Model):
  title = models.CharField(max_length=255)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

