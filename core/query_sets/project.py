from django.db import models
from django.http import Http404


class ProjectQuerySet(models.QuerySet):

    def for_user_or_404(self, project_id, user):
        try:
            return self.get(id=project_id, user=user)
        except self.model.DoesNotExist:
            raise Http404("Project not found.")

    def with_user(self, user):
        return self.filter(user=user)
