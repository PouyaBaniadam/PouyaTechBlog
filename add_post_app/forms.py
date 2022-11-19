from django import forms
from post_detail_app.models import Post
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "category_not_founded_1", "category_not_founded_2", "category_not_founded_3",
                  "category_not_founded_4", "category_not_founded_5", "body", "image",)
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (200 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "body": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (100000 characters)",
                       "style": "font-size: 20px; border-radius: 20px"}),
            "category": forms.SelectMultiple(attrs={"class": "form-control mr-0 ml-auto",
                                                    "style": "max-width: 300px; font-size: 20px; border-radius: 20px"}),
            "image": forms.FileInput(attrs={"class": "form-control mr-0 ml-auto",
                                            "style": "max-width: 350px; font-size:"
                                                     " 20px; border-radius: 15px"}),
            "category_not_founded_1": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px"}),
            "category_not_founded_2": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px"}),
            "category_not_founded_3": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px"}),
            "category_not_founded_4": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px"}),
            "category_not_founded_5": forms.Textarea(
                attrs={"class": "form-control mr-0 ml-auto", "placeholder": "Max length (50 characters)",
                       "style": "font-size: 20px"})
        }

    def clean(self):
        title = self.cleaned_data.get("title")
        try:
            post_exists = Post.objects.get(title=title)
        except:
            post_exists = "None"

        if post_exists != "None":
            raise ValidationError("This post title has been already taken!", code="same title")
