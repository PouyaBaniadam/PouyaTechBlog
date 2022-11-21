from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html


class Profile(models.Model):
    genders = [
        ("male", 'Male'),
        ("female", 'Female'),
        ("rather not to say", 'Rather not to say'),
    ]
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    username_label = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=genders, null=True, default="rather not to say")
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="Profile images", max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username.username

    def show_image(self):
        if self.image:
            return format_html(
                f'<a href="{self.image.url}" target="_blank" ><img src="{self.image.url}" width="60px" height="60px"></a>')

    show_image.short_description = "Images"
