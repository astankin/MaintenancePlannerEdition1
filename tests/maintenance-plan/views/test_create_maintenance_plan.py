from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from MaintenancePlanner import settings
from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel
from tests.common.test_data import create_equipment, create_user

AppUser = get_user_model()


class CreateMaintenancePlanViewTest(TestCase):
    def test_create_mp_when_user_is_loggedin_expect_to_create_report(self):
        user = create_user('MANAGER')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        form_data = {
            'name': 'TestMP',
            'equipment': create_equipment().id,
        }

        response = self.client.post(reverse('create-maintenance-plan'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MaintenancePlanModel.objects.count(), 1)
        created_service_report = MaintenancePlanModel.objects.first()
        self.assertEqual('TestMP', created_service_report.name)

    def test_create_mp_when_user_is_unauthenticated_expect_to_redirect_to_loggin_page(self):
        response = self.client.post(reverse('create-maintenance-plan'))
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create-maintenance-plan")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
