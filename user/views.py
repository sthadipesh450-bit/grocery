from .models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "add_user.html"
    success_url = reverse_lazy("user-list")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "update_user.html"
    success_url = reverse_lazy("user-list")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "delete_user.html"
    success_url = reverse_lazy("user-list")
