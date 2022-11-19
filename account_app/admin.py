from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username", "first_name", "last_name", "email", "gender", "birth_date", "show_image")
    list_filter = ("username", "email", "gender", "birth_date")
    search_fields = ("username", "email")
    search_help_text = "Search between titles and bodies..."
