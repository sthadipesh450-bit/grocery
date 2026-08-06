from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .form import SupplierForm
from .models import Suppliers


class SupplierListView(LoginRequiredMixin, ListView):
    model = Suppliers
    template_name = "suppliers/supplier_list.html"
    context_object_name = "suppliers"


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:supplier-list")


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Suppliers
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:supplier-list")


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Suppliers
    success_url = reverse_lazy("suppliers:supplier-list")
