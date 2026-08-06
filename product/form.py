from django import forms

from .models import Product


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
