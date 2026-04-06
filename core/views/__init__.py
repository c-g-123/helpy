from django.views.decorators.http import require_GET

from .agenda import agenda
from .authentication import register, register_submit, login, login_submit, logout
from .project import create_project, create_project_submit, project, edit_project, delete_project, projects
from .task import create_task, create_task_submit, task, edit_task, delete_task

from django.shortcuts import render


@require_GET
def index(request):
    return render(request, 'core/index.html')
