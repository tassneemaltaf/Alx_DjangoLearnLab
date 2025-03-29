from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import generic
from .models import Post

User = get_user_model

class RegisterView(CreateView):
  form_class = UserCreationForm #Uses Django’s built-in form for user registration.
  template_name = 'blog/register.html'  #Path to signup template
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

class ListView(generic.ListView):
  model = Post
  template_name = "blog/list_posts.html"
  context_object_name = 'posts'

class DetailView(generic.DetailView):
  model = Post
  template_name = "blog/view_posts.html"
  context_object_name = 'post'

class CreateView(LoginRequiredMixin, generic.CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = "blog/create_posts.html"
  success_url = reverse_lazy('posts')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class UpdateView(generic.UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = "blog/update_posts.html"
  context_object_name = 'post'
  success_url = reverse_lazy('posts')

class DeleteView(generic.DeleteView):
  model = Post
  template_name = "blog/delete_posts.html"
  context_object_name = 'post'
  success_url = reverse_lazy('posts')
