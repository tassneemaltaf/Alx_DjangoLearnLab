from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import RegisterView
from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path("", view=list_books, name="list_books"),
    path("library/", LibraryDetailView.as_view(), name="LibraryDetailView"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
