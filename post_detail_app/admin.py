from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title", "author", "is_allowed", "title", "created_at", "how_many_times_clicked", "updated_at", "show_image")
    list_filter = ("created_at", "updated_at", "is_allowed")
    search_fields = ("title", "body")
    search_help_text = "Search between titles and bodies..."


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "__str__", "created_at", "is_allowed")
    list_filter = ("post", "user", "is_allowed")
    search_fields = ("body",)
    search_help_text = "Search between posts..."


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")


@admin.register(DisLike)
class DisLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")


admin.site.register(Category)
