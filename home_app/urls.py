from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.search, name="search_posts"),
    path("profile/<slug:slug>/<int:pk>", views.profile, name="profile"),
    path("edit-profile", views.edit_profile, name="edit_profile"),
]
