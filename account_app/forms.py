from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError
import string

allowed_characters = []
for _ in string.ascii_letters:
    allowed_characters.append(_)
for __ in range(0, 10):
    allowed_characters.append(str(__))
allowed_characters.append("_")
allowed_characters.append("-")
allowed_characters.append("/")
allowed_characters.append("|")


class RegisterForm(forms.Form):
    username_for_register = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "style": "font-size:20px; margin-bottom: -5px"}))
    email_for_register = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "style": "font-size:20px; margin-bottom: -5px"}))
    password_for_register = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "style": "font-size:20px; margin-bottom: -5px"}))
    repeated_password_for_register = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Repeat password", "style": "font-size:20px; margin-bottom: -5px"}))

    def clean_username_for_register(self):
        username_for_register = self.cleaned_data.get("username_for_register")

        for item_checker in username_for_register:
            if item_checker not in allowed_characters:
                raise ValidationError(
                    "Unsupported format! (Just letters , numbers , '/' , '|' , '_' and '-' is allowed!)")

        try:
            username_exists = User.objects.get(username=username_for_register)
        except:
            username_exists = None

        if username_exists != None:
            raise ValidationError("This username has been already taken!")

        if len(str(username_for_register)) < 2:
            raise ValidationError("Username must have at least 2 characters!")

        if str(username_for_register).isnumeric():
            raise ValidationError("Username must have at least 1 letter!")

        return username_for_register

    def clean_email_for_register(self):
        email_for_register = self.cleaned_data.get("email_for_register")

        try:
            email_exists = User.objects.get(email=email_for_register)
        except:
            email_exists = None

        if email_exists is not None:
            raise ValidationError("This E-mail has been already taken!")

        return email_for_register

    def clean(self):
        password_for_register = self.cleaned_data.get("password_for_register")
        repeated_password_for_register = self.cleaned_data.get("repeated_password_for_register")

        if len(str(password_for_register)) < 8:
            raise ValidationError("Your password should have at least 8 characters!", code="8 char min")

        if str(password_for_register).isnumeric():
            raise ValidationError("Your password is entirely numeric!", code="just numbers")

        if str(password_for_register).isalpha():
            raise ValidationError("Your password doesn't contain letters!", code="just alphabets")

        if str(password_for_register) != str(repeated_password_for_register):
            raise ValidationError("Passwords do not match!", code="passwords dismatch")


class LoginForm(forms.Form):
    username_for_login = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "style": "font-size:20px"}))
    password_for_login = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "style": "font-size:20px"}))

    def clean_password_for_login(self):
        username_for_login = self.cleaned_data.get("username_for_login")
        password_for_login = self.cleaned_data.get("password_for_login")
        user = authenticate(username=username_for_login, password=password_for_login)

        if user is None:
            raise ValidationError("Your username or password is wrong!", code="invalid data")

        return username_for_login, password_for_login
