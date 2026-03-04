from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def create_task(request):
    return render(request, 'core/create_task.html')


@login_required
def task(request, task_id):
    return render(request, 'core/task.html')
