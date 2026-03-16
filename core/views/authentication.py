from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from core.forms import RegisterForm, LoginForm
from core.models import UserSettings


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "core/authentication/register.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username=username,
                password=password
            )

            UserSettings.objects.get_or_create(user=user)

            return _login_and_go_to_default_board(request, user)

        return render(request, "core/authentication/register.html", {"form": form})

    return HttpResponseNotAllowed(["GET", "POST"])


def login(request):
    if request.user.is_authenticated:
        return _login_and_go_to_default_board(request, request.user)

    if request.method == "GET":
        form = LoginForm()
        return render(request, "core/authentication/login.html", {"form": form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            authenticated_user = form.cleaned_data["authenticated_user"]
            return _login_and_go_to_default_board(request, authenticated_user)

        return render(request, "core/authentication/login.html", {"form": form})

    return HttpResponseNotAllowed(["GET", "POST"])


@login_required
def logout(request):
    auth.logout(request)
    return redirect("core:index")


def _login_and_go_to_default_board(request, user):
    auth.login(request, user)
    user_settings, _ = UserSettings.objects.get_or_create(user=user)
    return redirect(user_settings.get_default_board_url())
