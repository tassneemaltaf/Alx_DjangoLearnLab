from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("list_books")  # Redirect to the home page or another page
        return render(request, "relationship_app/register.html", {"form": form})

def list_books(request):
  books = Book.objects.all()
  context = {'list of book titles and their authors': books}
  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'

def get_context_data(self, **kwargs) -> dict[str, any]:
  context = super().get_context_data(**kwargs)
  library = self.get_object()
  context["books"] = Book.objects.filter(library=library)
  return context
