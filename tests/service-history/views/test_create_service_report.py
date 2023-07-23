from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from MaintenancePlanner import settings
from MaintenancePlanner.service_history.models import ServiceHistory
from tests.common.test_data import create_equipment, create_user

AppUser = get_user_model()


class CreateServiceReportViewTest(TestCase):
    def test_create_report_when_user_is_loggedin_expect_to_create_report(self):
        user = create_user('MANAGER')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        equipment = create_equipment()

        form_data = {
            'equipment': equipment.id,
            'problem_description': 'Some problem description',
            'solution': 'Some solution',
        }

        response = self.client.post(reverse('create-service-report'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ServiceHistory.objects.count(), 1)
        created_service_report = ServiceHistory.objects.first()
        self.assertEqual(created_service_report.equipment, equipment)

    def test_create_report_when_user_is_unauthenticated_expect_to_redirect_to_loggin_page(self):
        response = self.client.post(reverse('create-service-report'))
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create-service-report")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
