from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .form import CategoryForm, ProductForm
from .models import Category, Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:product-list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy("product:product-list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product:product-list")
    template_name = "product/product_confirm_delete.html"


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "product/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "product/category_form.html"
    success_url = reverse_lazy("product:category-list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "product/category_form.html"
    success_url = reverse_lazy("product:category-list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "product/category_confirm_delete.html"
    success_url = reverse_lazy("product:category-list")
