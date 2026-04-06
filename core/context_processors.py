def root_projects(request):
    if request.user.is_authenticated:
        return {
            "root_projects": request.user.projects.filter(parent_project=None)
        }

    return {}
