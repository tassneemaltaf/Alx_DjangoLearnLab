from django.shortcuts import render
from .models import Book
from .models import Library

def book_list(request):
  books = Book.objects.all()
  context = {'list of book titles and their authors': books}
  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'

def get_context_data(self, **kwargs) -> dict[str, Any]:
  context = super().get_context_data(**kwargs)
  library = self.get_object()
  context["books"] = Book.objects.filter(library=library)
  return context
