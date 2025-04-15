from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(null=True)

class Author(models.Model):
  name = models.CharField(max_length=255);

  def __str__(self):
        return self.name

class Book(models.Model):
  title = models.CharField(max_length=255);
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")

  def __str__(self):
        return self.name

class Library(models.Model):
  name = models.CharField(max_length=255)
  books = models.ManyToManyField(Book, related_name="books")

  def __str__(self):
        return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=255);
  library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

  def __str__(self):
        return self.name