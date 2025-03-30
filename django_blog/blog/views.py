from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import generic
from .models import Post
from .forms import CommentForm

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
  template_name = "blog/post_list.html"
  context_object_name = 'posts'

class DetailView(generic.DetailView):
  model = Post
  template_name = "blog/post_detail.html"
  context_object_name = 'post'

class CreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = "blog/post_form.html"
  success_url = reverse_lazy('posts')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = "blog/post_update.html"
  context_object_name = 'post'
  success_url = reverse_lazy('posts')

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
  model = Post
  template_name = "blog/post_delete.html"
  context_object_name = 'post'
  success_url = reverse_lazy('posts')
