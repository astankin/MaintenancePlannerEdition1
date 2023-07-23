from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.shortcuts import reverse

from MaintenancePlanner.accounts.decorators import unauthenticated_user, allowed_users
from MaintenancePlanner.accounts.models import Profile
from MaintenancePlanner.accounts.views import register

AppUser = get_user_model()


class RegisterViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AppUser.objects.create_user(
            username='astankin',
            password='password123@',
            role='MANAGER',
        )

    def test_when_user_is_created_profile_is_created(self):
        created_profile = Profile.objects.filter(id=self.user.id).get()
        self.assertEqual('astankin Profile', str(created_profile))


    def test_unauthenticated_user_redirect_to_home_page(self):
        request = self.factory.get(reverse('register'))
        request.user = self.user

        decorated_view_func = unauthenticated_user(register)

        response = decorated_view_func(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home-page'))

    def test_user_with_allowed_role(self):
        request = self.factory.get(reverse('register'))
        request.user = self.user

        decorated_view_func = allowed_users(['MANAGER'])(register)

        response = decorated_view_func(request)
        self.assertEqual(response.status_code, 200)

    def test_user_with_not_allowed_role_redirect(self):
        request = self.factory.get(reverse('register'))
        request.user = self.user

        decorated_view_func = allowed_users(['OPERATOR'])(register)

        response = decorated_view_func(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home-page'))
