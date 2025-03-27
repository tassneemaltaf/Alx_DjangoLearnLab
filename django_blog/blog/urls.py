from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView, submit, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', TemplateView.as_view(template_name='blog/base.html'), name='home'),
  path('posts/', submit, name='posts'),
  path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  path('post/', ListView.as_view(), name='list_view'),
  path('post/new/', CreateView.as_view(), name='create_view'),
  path('post/<int:pk>/', DetailView.as_view(), name='detail_view'),
  path('post/<int:pk>/update/', UpdateView.as_view(), name='update_view'),
  path('post/<int:pk>/delete/', DeleteView.as_view(), name='delete_view'),
]
