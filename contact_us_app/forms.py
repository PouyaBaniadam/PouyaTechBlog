from django import forms
from django.core.exceptions import ValidationError


class MessageForm(forms.Form):
    name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={"class": 'form-control mr-0 ml-auto', "style": "font-size: 22px; border-radius: 20px",
               "placeholder": "Max length (70 characters)"}))
    subject = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={"class": 'form-control mr-0 ml-auto', "style": "font-size: 22px; border-radius: 20px",
               "placeholder": "Max length (70 characters)"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": 'form-control mr-0 ml-auto', "style": "font-size: 22px; border-radius: 20px",
               "placeholder": "Max length (∞ characters)"}))
    message = forms.CharField(max_length=5000, widget=forms.Textarea(
        attrs={"class": 'form-control mr-0 ml-auto', "style": "font-size: 22px; border-radius: 20px",
               "rows": 5,
               "placeholder": "Max length (5000 characters)"}))
