from django import forms

from .models import Suppliers


class SupplierForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Supplier Name"}),
        label="Supplier Name",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}),
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}),
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Enter Address"}),
    )

    class Meta:
        model = Suppliers
        fields = ["name", "email", "phone_number", "address", "is_active"]
