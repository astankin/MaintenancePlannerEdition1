from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase, RequestFactory
from django.urls import reverse

from MaintenancePlanner.accounts.views import profile_update

AppUser = get_user_model()


class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AppUser.objects.create_user(
            username='astankin',
            password='testpassword123',
        )

    def test_authenticated_user_can_access_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile-update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-update.html')

    def test_unauthenticated_user_redirect(self):
        response = self.client.get(reverse('profile-update'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/login/?next=/user/profile/update/')

    def test_form_submission_failure(self):
        self.client.force_login(self.user)
        data = {
            'username': '',
        }
        response = self.client.post(reverse('profile-update'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-update.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)
