from django.contrib import admin
from django.contrib.auth.models import User

from core.models import Task, Project, Tag, Resource


admin.register(User)
admin.register(Project)
admin.register(Task)
admin.register(Tag)
admin.register(Resource)
