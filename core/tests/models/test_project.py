from django.test import TestCase
from django.contrib.auth.models import User

from core.models.project import Project

class ProjectModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.project = Project.objects.create(user=self.user, name='Test_Project')

    def test_project_name(self):
        self.assertEqual(self.project.name, 'Alpha Project')

    def test_user_creation(self):
        self.assertEqual(self.project.user, self.user)

    def test_project_name_is_str(self):
        self.assertEqual(str(self.project), 'Alpha Project')