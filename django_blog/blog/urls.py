from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterView
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
  path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', TemplateView.as_view(template_name='blog/base.html'), name='home'),
  path('', TemplateView.as_view(template_name='blog/base.html'), name='posts'),
]
