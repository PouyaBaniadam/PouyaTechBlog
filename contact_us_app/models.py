from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message[:30]}..."


class ContactUsInfo(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    who_are_we = models.TextField(max_length=500)
    telegram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.who_are_we[:75]}"
