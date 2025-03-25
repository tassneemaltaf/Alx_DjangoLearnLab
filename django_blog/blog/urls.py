from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView, submit
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', TemplateView.as_view(template_name='blog/base.html'), name='home'),
  path('posts/', submit, name='posts'),
  path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done')
]
