from django.test import TestCase
from django.contrib.auth import get_user_model

from MaintenancePlanner.accounts.forms import UserUpdateForm

User = get_user_model()


class UserUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='astankin',
            email='astankin@abv.bg',
            role='MANAGER'
        )

    def test_user_update_form_save_with_valid_data(self):
        data = {
            'username': 'astankin_updated',
            'first_name': 'Atanas',
            'last_name': 'Stankin',
            'email': 'updated_astankin@abv.bg'
        }
        form = UserUpdateForm(data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_update_form_save_with_missing_required_field(self):
        data = {}
        form = UserUpdateForm(data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
