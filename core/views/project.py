from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from core.forms import ProjectForm
from core.models import Project, Task


@login_required
def create_project(request):
    if request.method == 'GET':
        form = ProjectForm()
    elif request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect(reverse('core:project', args=[project.id]))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request,'core/project/create-project.html', {'form': form})


@login_required
def view_project(request, project_id):
    project = Project.objects.for_user_or_404(project_id, request.user)

    if request.method == 'GET':
        form = ProjectForm(instance=project)
    elif request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            project = form.save()
            return redirect(reverse('core:project', args=[project.id]))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    tasks = Task.objects.active_top_level_from_project(project)

    context = {
        'project': project,
        'tasks': tasks,
        'form': form,
    }

    return render(request, 'core/project/project.html', context)


@login_required
def view_projects(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    projects = Project.objects.with_user(request.user)
    return render(request, 'core/project/projects.html', {'projects': projects})
