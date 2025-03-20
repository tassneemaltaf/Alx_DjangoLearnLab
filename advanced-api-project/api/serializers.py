from rest_framework import serializers
from .models import Book, Author

#This is the Book serializer, it contains a validation to verify if the publication year is not greater than the current year
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'publication_year', 'author']
  
  def validate(self, data):
    if data['publication_year'] > 2025:
      raise serializers.ValidationError("Invalid year.")
    return data
  
#This is the Author serializer, it contains a nested book serializer, this allows the api to return the author data along with its related books
class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ['name', 'books']
