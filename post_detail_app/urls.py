from django.urls import path
from . import views

app_name = "post_detail_app"

urlpatterns = [
    path("details/<slug:slug>", views.post_detail, name="post_detail"),
    path("category/<int:pk>", views.category_detail, name="category_detail"),
    path("like/<slug:slug>/<int:pk>", views.like, name="like"),
    path("dislike/<slug:slug>/<int:pk>", views.dislike, name="dislike"),
    path("dislike/<slug:slug>/<int:pk>", views.dislike, name="dislike"),
]
