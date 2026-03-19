from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Project, Task, Tag

class TagModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@email.com', password='test_password')
        self.project = Project.objects.create(user=self.user, name='test_Project')
        self.task = Task.objects.create(project=self.project, name='test_task')

        self.tag = Tag.objects.create(name='test_tag')

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, 'test_tag')
  