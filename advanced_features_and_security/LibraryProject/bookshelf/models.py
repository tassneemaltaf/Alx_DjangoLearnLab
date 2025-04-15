from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
  def create_user():
    ...
  
  def create_superuser():
    ...

class CustomUser(AbstractUser):
  date_of_birth = models.DateField()
  profile_photo = models.ImageField(null=True)

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()
