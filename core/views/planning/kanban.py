from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def kanban(request):
    return render(request, 'core/planning/kanban.html')
