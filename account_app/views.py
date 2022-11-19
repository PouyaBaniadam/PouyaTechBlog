from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account_app.forms import LoginForm, RegisterForm
from account_app.models import Profile


def leave(request):
    logout(request)
    return redirect("/")


def join(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.user.is_authenticated:
        return redirect("/")

    # register logic
    if request.method == "POST" and request.POST.get("username_for_register"):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username_for_register = register_form.cleaned_data.get('username_for_register')
            username_for_register = str(username_for_register).lower()
            email_for_register = register_form.cleaned_data.get('email_for_register')
            password_for_register = register_form.cleaned_data.get('password_for_register')

            user = User.objects.create_user(username=username_for_register, password=password_for_register,
                                            email=email_for_register)
            login(request, user)
            Profile.objects.create(username=request.user, username_label=request.user.username,
                                   email=email_for_register, password=password_for_register)
            return redirect(f"profile/{request.user.username}/{request.user.id}")

    # Login logic
    if request.method == "POST" and request.POST.get("username_for_login"):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = User.objects.get(username=login_form.cleaned_data.get("username_for_login"))
            login(request, user)
            return redirect(f"profile/{request.user.username}/{request.user.id}")

    return render(request, "account_app/index.html",
                  context={"login_form": login_form, "register_form": register_form})
