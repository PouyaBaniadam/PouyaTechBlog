from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from account_app.models import Profile
import datetime
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

birth_date_choices = []

for _ in range(datetime.datetime.today().year - 101, datetime.datetime.today().year):
    birth_date_choices.append(_)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "username_label", "first_name", "last_name", "bio", "email", "image", "gender", "birth_date",
            "phone_number")
        widgets = {
            "username_label": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (200 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "first_name": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "last_name": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "bio": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (100 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (∞ characters)",
                       "style": "font-size: 20px; border-radius: 20px; color: red; border-color: red"}),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (20 characters)",
                       "style": "font-size: 20px; border-radius: 20px; color: red; border-color: red"}),
            "image": forms.FileInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (75 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "gender": forms.Select(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (75 characters)",
                       "style": "font-size: 20px; border-radius: 20px; color: red; border-color: red"}),
            "birth_date": forms.SelectDateWidget(years=birth_date_choices,
                                                 attrs={"class": "form-control mr-0 ml-auto",
                                                        "placeholder": "Max length (75 characters)",
                                                        "style": "font-size: 20px; border-radius: 20px;"
                                                                 "color: red; border-color: red"}),
        }

    def clean_username_label(self):
        user_name = self.cleaned_data.get("username_label")

        if len(str(user_name)) < 2:
            raise ValidationError("Username must have at least 2 characters!")

        if str(user_name).isnumeric():
            raise ValidationError("Username must have at least 1 letter!")

        for single_character_checker in user_name:
            if single_character_checker not in allowed_characters:
                raise ValidationError(
                    "Unsupported format! (Just letters , numbers , '/' , '|' , '_' and '-' is allowed!)")

        return user_name

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            email_exists = User.objects.get(email=email)
            email_exists = email_exists.email
        except:
            email_exists = None

        if email_exists is not None and email_exists != self.cleaned_data.get("email"):
            raise ValidationError("This E-mail has been already taken!")

        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if len(str(first_name)) < 2:
            raise ValidationError("First name must have at least 2 characters!")

        if not str(first_name).isalpha():
            raise ValidationError("First name must only contain letters!")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")

        if len(str(last_name)) < 2:
            raise ValidationError("Last name name must have at least 2 characters!")

        if not str(last_name).isalpha():
            raise ValidationError("Last name name must only contain letters!")

        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        try:
            phone_number_exists = Profile.objects.get(phone_number=phone_number)
            phone_number_exists = phone_number_exists.phone_number
        except:
            phone_number_exists = None

        if phone_number_exists is not None and phone_number_exists != self.cleaned_data.get("phone_number"):
            raise ValidationError("This Phone number has been already taken!")

        return phone_number

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if last_name is None and first_name is not None:
            raise ValidationError("If you have a first name , You should fill your last name too!")
        elif first_name is None and last_name is not None:
            raise ValidationError("If you have a last name , You should fill your first name too!")
