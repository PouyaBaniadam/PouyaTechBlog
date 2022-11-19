from django.urls import path
from . import views

app_name = "contact_us_app"

urlpatterns = [
    path("contact_us", views.contact_us, name="contact_us"),
]
