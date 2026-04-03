from django.views.decorators.http import require_GET

from .planning import agenda
from .authentication import register, register_submit, login, login_submit, logout
from .project import create_project, create_project_submit, project, edit_project, delete_project, projects
from .task import create_task, create_task_submit, task, edit_task, delete_task

from django.shortcuts import render, redirect


@require_GET
def index(request):
    if request.user.is_authenticated:
        return redirect(request.user.usersettings.get_default_board_url())

    return render(request, 'core/index.html')
