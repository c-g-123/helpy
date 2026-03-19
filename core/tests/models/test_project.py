from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Project

class ProjectModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@email.com', password='test_password')
        self.project = Project.objects.create(user=self.user, name='Test_Project')

    def test_project_name(self):
        self.assertEqual(self.project.name, 'Test_Project')

    def test_user_assigned_to_project(self):
        self.assertEqual(self.project.user, self.user)

    def test_project_name_is_str(self):
        self.assertEqual(str(self.project), 'Test_Project')

    def test_project_delete_user_cascades_projects(self):
        self.user.delete()
        self.assertEqual(Project.objects.count(), 0)