from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    category_not_founded_1 = models.CharField(max_length=30, null=True, blank=True)
    category_not_founded_2 = models.CharField(max_length=30, null=True, blank=True)
    category_not_founded_3 = models.CharField(max_length=30, null=True, blank=True)
    category_not_founded_4 = models.CharField(max_length=30, null=True, blank=True)
    category_not_founded_5 = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(max_length=100000)
    is_allowed = models.BooleanField(default=False)
    image = models.ImageField(upload_to="post images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    how_many_times_clicked = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, editable=False)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html(
            f'<a href="{self.image.url}" target="_blank" ><img src="{self.image.url}" width="60px" height="60px"></a>')

    show_image.short_description = "Images"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_allowed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.body[:30]}..."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.post} - {self.created_at}"

    class Meta:
        ordering = ("-created_at",)


class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dislikes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislikes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.post} - {self.created_at}"

    class Meta:
        ordering = ("-created_at",)
