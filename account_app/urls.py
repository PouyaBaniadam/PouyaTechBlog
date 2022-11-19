from django.urls import path
from . import views

app_name = "account_app"

urlpatterns = [
    path("leave", views.leave, name="leave"),
    path("join", views.join, name="join"),
]
