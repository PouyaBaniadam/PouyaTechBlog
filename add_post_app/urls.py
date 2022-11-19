from django.urls import path
from . import views

app_name = "post_add_app"

urlpatterns = [
    path("", views.add_post, name="add_post"),
]
