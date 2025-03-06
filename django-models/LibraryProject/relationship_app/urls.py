from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path("", view=book_list, name="book_list"),
    path("", view=LibraryDetailView, name="LibraryDetailView")
]
