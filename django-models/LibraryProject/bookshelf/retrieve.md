retrieved_book = Book.objects.get(title=book.title)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
###1984 George Orwell 1949
