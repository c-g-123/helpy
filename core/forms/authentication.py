from django import forms
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username",}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password",}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Repeat password",}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        repeat_password = cleaned_data["repeat_password"]

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username",}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password",}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data["username"]
        password = cleaned_data["password"]

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Invalid username or password.")
            if not user.is_active:
                raise forms.ValidationError("Your account is disabled.")

            cleaned_data["authenticated_user"] = user

        return cleaned_data
