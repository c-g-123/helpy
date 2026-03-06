from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse

from core.forms import ProjectForm


@login_required
def create_project(request):
    context = {}

    if request.method == "GET":
        form = ProjectForm()
        context['form'] = form
        return render(request, 'core/create_project.html', context)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        context['form'] = form
        if form.is_valid():
            project = form.save(commit=False)
            project.user_id = request.user
            project.save()
            return redirect(reverse("core:project", args=[project.id]))

        return render(request, "core/create_project.html", context)

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def view_project(request, project_id):
    return render(request, 'core/project.html')
