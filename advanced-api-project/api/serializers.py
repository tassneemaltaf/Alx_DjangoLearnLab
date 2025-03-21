from rest_framework import serializers
from .models import Book, Author
import datetime

#This is the Book serializer, it contains a field-level validation method to verify if the publication year is not in the future
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'publication_year', 'author']
  
  def validate_publication_year(self, value):
    current_year = datetime.date.today().year
    if value > current_year:
      raise serializers.ValidationError("Invalid year.")
    return value
  
#This is the Author serializer, it contains a nested book serializer, this allows the api to return the author data along with its related books
class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ['name', 'books']
