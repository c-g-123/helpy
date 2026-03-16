from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Task


@login_required
def kanban(request):

    tasks_todo = Task.objects.filter(status=Task.Status.TODO)
    tasks_in_progress = Task.objects.filter(status=Task.Status.IN_PROGRESS)
    tasks_done= Task.objects.filter(status=Task.Status.DONE)

    context = {
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_done': tasks_done
        }

    return render(request, 'core/planning/kanban.html', context)
