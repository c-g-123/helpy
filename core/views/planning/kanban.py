from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Task


@login_required
def kanban(request):

    tasks_todo = Task.objects.filter(status=Task.Status.TODO, project_id__user_id=request.user, parent_task__isnull=True) # Only show top-level tasks in the kanban view. Subtasks will be shown on the task detail page.
    tasks_in_progress = Task.objects.filter(status=Task.Status.IN_PROGRESS, project_id__user_id=request.user, parent_task__isnull=True)
    tasks_done= Task.objects.filter(status=Task.Status.DONE, project_id__user_id=request.user, parent_task__isnull=True)

    context = {
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_done': tasks_done
        }

    return render(request, 'core/planning/kanban.html', context)
