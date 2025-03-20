from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class ListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
  queryset = Book.objects.filter(id=id)

class CreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
