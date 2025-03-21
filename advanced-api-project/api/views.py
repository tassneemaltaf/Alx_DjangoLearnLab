from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import serializers
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

#The first view is to list the books view, it has permissions to read only for unauthenticated users, and requires authentication for any modification operation
#It also contains a search filter, that we can use to add to the URL, if we want specific book with a specific title or from a specific author
class ListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['title', 'author']
  ordering_fields = ['publication_year']

#This is to list a specific book based on its primary key
#Permissions are same as list
class DetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

#This is the create view that has a perform create method that checks if there's a title entered by the user, and raises an error if not
#Also Authentication is needed to use this
class CreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    if not title:
      raise serializers.ValidationError("Title cannot be empty.")
    # Assign the logged-in user to the book
    serializer.save(user=self.request.user)
    return super().perform_create(serializer)

#This is the update method that has the perform update method that checks if the title that is updated has more than 4 characters, and raises an error if not
class UpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

  def perform_update(self, serializer):
    title = serializer.validated_data.get('title')
    if len(title) < 4:
      raise serializers.ValidationError("Title can't be short")
    return super().perform_update(serializer)

#this is a delete view that deletes a specific user based on its id
#and also needs authentication to be used
class DeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]
