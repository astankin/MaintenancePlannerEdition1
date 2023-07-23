from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse

from MaintenancePlanner import settings
from MaintenancePlanner.accounts.views import login_user
from tests.common.test_data import create_user

AppUser = get_user_model()


class LoginUserViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_user()

    def test_authenticated_user_redirect(self):
        request = self.factory.get('/login/')
        request.user = self.user
        response = login_user(request)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', fetch_redirect_response=False)

        redirected_response = self.client.get(response.url, follow=True)
        self.assertEqual(redirected_response.status_code, 200)

    def test_valid_credentials_login(self):
        credentials = {
            'username': 'astankin',
            'password': 'password123'
        }
        response = self.client.post(reverse('login'), data=credentials)
        self.assertEqual(response.status_code, 302)
        self.assertEqual('/', response.headers.get('Location'))

