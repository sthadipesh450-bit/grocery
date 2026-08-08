from django import forms

from user.models import User


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username and User.objects.filter(username=username).exists():
            self.add_error("username", "This username is already in use.")
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
