from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    order_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Order
        fields = ["customer", "order_date", "status", "order_details"]
        widgets = {
            "order_details": forms.CheckboxSelectMultiple,
        }
