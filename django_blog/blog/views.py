from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
  form_class = UserCreationForm #Uses Django’s built-in form for user registration.
  template_name = 'registration/register.html'  #Path to signup template
  success_url = reverse_lazy('login')  #Redirects to login after signup