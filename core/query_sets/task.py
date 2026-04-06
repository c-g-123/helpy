from django.db import models


class TaskQuerySet(models.QuerySet):

    def for_user(self, user):
        return self.filter(project__user=user)

    def top_level(self, user):
        return self.for_user(user).filter(parent_task__isnull=True)
