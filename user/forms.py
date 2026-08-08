from django import forms
from .models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter username"}),
        label="Username",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
        label="Password",
    )

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "address", "role", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
