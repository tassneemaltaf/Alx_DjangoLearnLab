from bookshelf.models import Book
book.delete()
###(1, {'bookshelf.Book': 1})
Book.objects.filter(title=book.title).exists()
###False
