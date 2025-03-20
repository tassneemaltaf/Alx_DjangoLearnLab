from django.urls import path
from .views import ListView, CreateView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path("books/", view=ListView.as_view(), name="list_view"),
    path("books/<int:pk>/", view=DetailView.as_view(), name="detail_view"),
    path("books/create/", view=CreateView.as_view(), name="create_view"),
    path("books/update/", view=UpdateView.as_view(), name="update_view"),
    path("books/delete/<int:pk>/", view=DeleteView.as_view(), name="delete_view"),
]
