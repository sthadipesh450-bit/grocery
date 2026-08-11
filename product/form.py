from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Product Name"}),
        label="Product Name",
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Enter Description"}),
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"placeholder": "Enter Price"}),
    )
    quantity = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={"placeholder": "Enter Quantity"}),
    )

    class Meta:
        model = Product
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Category Name"}),
        label="Category Name",
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Enter Description"}),
    )

    class Meta:
        model = Category
        fields = ("category_name", "description")
