from django.test import TestCase

from MaintenancePlanner.accounts.forms import UserRegisterForm


class UserRegisterFormTest(TestCase):

    def test_user_register_form_save_with_valid_data(self):
        data = {
            'username': 'astankin',
            'email': 'astankin@abv.bg',
            'role': 'MANAGER',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        form = UserRegisterForm(data)

        self.assertTrue(form.is_valid())

    def test_user_register_form_save_with_invalid_data(self):
        data = {
            'username': 'astankin',
            'email': 'astankin@abv.bg',
            'role': 'MANAGER',
            'password1': 'test',
            'password2': 'test',
        }
        form = UserRegisterForm(data)

        self.assertFalse(form.is_valid())

    def test_user_register_form_missing_required_field(self):
        data = {}
        form = UserRegisterForm(data)
        self.assertFalse(form.is_valid())
        self.assertIsNotNone('username', form.errors)
        self.assertIsNotNone('email', form.errors)
        self.assertIsNotNone('role', form.errors)
        self.assertIsNotNone('password1', form.errors)
        self.assertIsNotNone('password2', form.errors)

    def test_user_register_form_passwords_mismatch(self):
        data = {
            'username': 'astankin',
            'email': 'astankin@abv.bg',
            'role': 'MANAGER',
            'password1': 'testpass123',
            'password2': 'testpass1234',
        }
        form = UserRegisterForm(data)
        self.assertFalse(form.is_valid())
        self.assertIsNotNone('password2', form.errors)

