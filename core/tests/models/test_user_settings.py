from django.test import TestCase
from django.contrib.auth.models import User
from core.models import UserSettings


class UserSettingsModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@email.com', password='test_password')
        self.user_settings = UserSettings.objects.create(
            user=self.user,
            theme=UserSettings.Theme.DARK,
            default_board=UserSettings.DefaultBoard.KANBAN
        )

    def test_user_settings_theme(self):
        self.assertEqual(self.user_settings.theme, 'DARK')

    def test_user_settings_defaut_board(self):
        self.assertEqual(self.user_settings.default_board, 'KANBAN')

    def test_user_settings_name_is_str(self):
        self.assertEqual(str(self.user_settings), "test_user's settings")