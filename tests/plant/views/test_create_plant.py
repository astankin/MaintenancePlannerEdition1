from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from MaintenancePlanner import settings
from MaintenancePlanner.plant.models import Plant
from tests.common.test_data import create_equipment, create_user

AppUser = get_user_model()


class CreatePlantViewTest(TestCase):
    def test_create_plant_when_manager_user_is_loggedin_expect_to_create_plant(self):
        user = create_user('MANAGER')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        form_data = {
            'name': 'TestPlant',
            'country': 'Bulgaria',
            'city': 'Plovdiv',
            'address': 'Address',
            'cost_center': 'BG20',
            'equipment': create_equipment().id,

        }

        response = self.client.post(reverse('create-plant'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Plant.objects.count(), 2)
        created_service_report = Plant.objects.first()
        self.assertEqual('TestPlant', created_service_report.name)

    def test_create_report_when_user_is_unauthenticated_expect_to_redirect_to_loggin_page(self):
        response = self.client.post(reverse('create-plant'))
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create-plant")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
