from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def create_project(request):
    return render(request, 'core/create_project.html')


@login_required
def project(request, project_id):
    return render(request, 'core/project.html')
