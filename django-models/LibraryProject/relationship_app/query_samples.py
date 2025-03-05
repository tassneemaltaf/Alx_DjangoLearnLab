from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
  author = Author.objects.get(name=author_name)
  books = Book.objects.filter(author=author)
  print([book.title for book in books])

def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  books = library.books.all() 
  print([book.title for book in books])

def get_librarian_for_library(library_name):
    Librarian.objects.get(library=library_name);
    print(Librarian.name)