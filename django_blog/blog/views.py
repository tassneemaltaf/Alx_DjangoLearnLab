from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model

class RegisterView(CreateView):
  form_class = UserCreationForm #Uses Django’s built-in form for user registration.
  template_name = 'registration/register.html'  #Path to signup template
  success_url = reverse_lazy('login')  #Redirects to login after signup

@login_required
def profile_view(request):
  return render(request, 'accounts/profile.html')

def submit(request):
  if request.method == "POST":
    user = request.user
    user.username = request.POST["username"]
    user.save()
    return redirect("profile")
  return render(request, "blog/profile.html", {"msg": "username updated"})
