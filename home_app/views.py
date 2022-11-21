from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from account_app.models import Profile
from home_app.forms import ProfileEditForm
from post_detail_app.models import Category, Post
from post_detail_app import models as post_detail_app_models
import datetime
from datetime import datetime

today = (datetime.today().date())


def home(request):
    post_objects = post_detail_app_models.Post.objects.order_by("-created_at")
    page_number = request.GET.get('page')
    paginator = Paginator(post_objects, 10)
    objects_list = paginator.get_page(page_number)
    all_authors = User.objects.all()

    return render(request, "home_app/index.html",
                  context={"post_objects": objects_list, "today": today, "all_authors": all_authors})


def category_detail(request, pk=None):
    category = Category.objects.get(id=pk)
    post_objects = category.article_set.all()
    return render(request, "home_app/index.html", context={"post_objects": post_objects})


def search(request):
    q = request.GET.get("q")
    post_objects = Post.objects.filter(title__icontains=q)

    if len(post_objects) == 0:
        post_objects = Post.objects.filter(body__icontains=q)

    page_number = request.GET.get('page')
    paginator = Paginator(post_objects, 10)
    objects_list = paginator.get_page(page_number)
    all_authors = User.objects.all()

    return render(request, "home_app/index.html", context={"post_objects": objects_list, "all_authors": all_authors})


def profile(request, slug, pk):
    if request.user.is_authenticated:

        post_datas = Post.objects.filter(author=pk, is_allowed=True).order_by("-created_at")
        page_number = request.GET.get('page')
        paginator = Paginator(post_datas, 10)
        post_list = paginator.get_page(page_number)
        personal_data = User.objects.get(username=slug)
        all_users = User.objects.all()
        return render(request, "home_app/profile.html",
                      context={"post_datas": post_datas, "personal_data": personal_data, "all_users": all_users,
                               "post_list": post_list})

    else:
        return redirect("account_app:join")


def edit_profile(request):
    if request.user.is_authenticated:
        username_taken = "0"
        email_taken = "0"
        profile = Profile.objects.get(username=request.user)
        profile_edit_form = ProfileEditForm(instance=profile)
        if request.method == "POST":
            profile_edit_form = ProfileEditForm(request.POST, request.FILES,
                                                instance=profile)
            if profile_edit_form.is_valid():
                all_usernames = []
                for _ in User.objects.all():
                    all_usernames.append(_.username)
                all_emails = []
                for _ in User.objects.all():
                    all_emails.append(_.email)
                # if profile_edit_form.cleaned_data.get("username_label") in all_usernames:
                if profile_edit_form.cleaned_data.get("username_label") == str(request.user):
                    user_to_be_saved = User.objects.get(username=request.user)
                    user_to_be_saved.username = profile_edit_form.cleaned_data.get("username_label")
                    user_to_be_saved.first_name = profile_edit_form.cleaned_data.get("first_name")
                    user_to_be_saved.last_name = profile_edit_form.cleaned_data.get("last_name")
                    user_to_be_saved.email = profile_edit_form.cleaned_data.get("email")
                    user_to_be_saved.save()
                    profile_edit_form.save()
                    return redirect("home_app:edit_profile")
                else:
                    if profile_edit_form.cleaned_data.get("username_label") in all_usernames:
                        username_taken = "This username has been already taken!"
                    else:
                        user_to_be_saved = User.objects.get(username=request.user)
                        user_to_be_saved.username = profile_edit_form.cleaned_data.get("username_label")
                        user_to_be_saved.first_name = profile_edit_form.cleaned_data.get("first_name")
                        user_to_be_saved.last_name = profile_edit_form.cleaned_data.get("last_name")
                        user_to_be_saved.email = profile_edit_form.cleaned_data.get("email")
                        user_to_be_saved.save()
                        profile_edit_form.save()
                        return redirect("home_app:edit_profile")

                return render(request, "home_app/edit_profile.html",
                              context={"profile_edit_form": profile_edit_form, "username_taken": username_taken})

        return render(request, "home_app/edit_profile.html",
                      context={"profile_edit_form": profile_edit_form})

    else:
        return redirect("home_app:home")


def delete_profile(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect("home_app:home")
