from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .form import CustomerForm
from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customer/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"
    success_url = reverse_lazy("customer:customer-list")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"
    success_url = reverse_lazy("customer:customer-list")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy("customer:customer-list")
    template_name = "customer/customer_confirm_delete.html"
