from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView, submit, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', TemplateView.as_view(template_name='blog/home.html'), name='home'),
  path('save/', submit, name='save'),
  path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  path('posts/', ListView.as_view(), name='posts'),
  path('post/new/', CreateView.as_view(), name='create_view'),
  path('post/<int:pk>/', DetailView.as_view(), name='detail_view'),
  path('post/<int:pk>/update/', UpdateView.as_view(), name='update_view'),
  path('post/<int:pk>/delete/', DeleteView.as_view(), name='delete_view'),
]
