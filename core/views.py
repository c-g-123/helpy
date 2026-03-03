from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse


def home(request):
    return render(request, 'core/home.html')


def login(request):
    if request.method != 'POST':
        return render(request, 'core/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    context = {}

    if not user:
        context['error_message'] = 'Invalid username or password.'
        return render(request, 'core/login.html', context)

    if not user.is_active:
        context['error_message'] = 'Your account is disabled.'
        return render(request, 'core/login.html', context)

    auth.login(request, user)
    return redirect(reverse('core:calendar'))  # Change this to redirect to the default dashboard chosen by the user.


def register(request):
    return render(request, 'register.html')


@login_required
def calendar(request):
    return render(request, 'calendar.html')


@login_required
def agenda(request):
    return render(request, 'agenda.html')


@login_required
def kanban(request):
    return render(request, 'kanban.html')


@login_required
def project(request, project_id):
    return render(request, 'project.html')


@login_required
def create_project(request):
    return render(request, 'project.html')


@login_required
def task(request, task_id):
    return render(request, 'task.html')


@login_required
def create_task(request):
    return render(request, 'task.html')


@login_required
def account(request):
    return render(request, 'account.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('core:home'))
