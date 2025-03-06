from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="list_books"),
    path("", view=LibraryDetailView, name="LibraryDetailView")
]
