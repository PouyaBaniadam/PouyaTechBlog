from django.contrib import admin
from .models import *


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "__str__", "created_at")
    search_fields = ("name",)
    search_help_text = "Search between names..."


@admin.register(ContactUsInfo)
class ContactUsInfoAdmin(admin.ModelAdmin):
    list_display = ("address", "telegram", "youtube", "instagram", "email", "__str__")
