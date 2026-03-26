from django.db import models
from django.http import Http404


class TaskQuerySet(models.QuerySet):

    def for_user_or_404(self, task_id, user):
        try:
            return self.get(id=task_id, project__user=user)
        except self.model.DoesNotExist:
            raise Http404("Task not found.")

    def subtasks_of(self, task):
        return self.filter(parent_task=task)

    def active_top_level_from_project(self, project):
        to_do_tasks = self.filter(project=project, parent_task__isnull=True, status=self.model.Status.TO_DO)
        in_progress_tasks = self.filter(project=project, parent_task__isnull=True, status=self.model.Status.IN_PROGRESS)
        return to_do_tasks.union(in_progress_tasks)
