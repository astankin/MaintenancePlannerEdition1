from django.core.exceptions import ValidationError
from django.test import TestCase, RequestFactory
from django.urls import reverse

from MaintenancePlanner import settings
from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.equipment.views import CreateEquipment
from tests.common.test_data import create_plant, create_department, create_user, create_equipment


class CreateEquipmentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.plant = create_plant()
        self.department = create_department()

    def test_authenticated_manager_can_create_equipment(self):
        user = create_user('MANAGER')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)
        request = self.client.get(reverse('create-equipment'))
        request.user = user

        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'create-equipment.html')

    def test_authenticated_operator_can_not_create_equipment(self):
        user = create_user('SUPERVISOR')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)
        request = self.client.get(reverse('create-equipment'))
        request.user = user

        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'create-equipment.html')

    def test_authenticated_supervisor_can_create_equipment(self):
        user = create_user('OPERATOR')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)
        request = self.client.get(reverse('create-equipment'))
        request.user = user

        self.assertEqual(302, request.status_code)
        self.assertEqual('/', request.headers.get('Location'))

    def test_equipment_creation_if_user_is_unauthenticated_redirect(self):
        response = self.client.post(reverse('create-equipment'))
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create-equipment")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))

    def test_create_equipment_when_user_is_loggedin_expect_to_create_equipment(self):
        user = create_user('MANAGER')
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        Equipment.objects.create(
            description='TestEquipment',
            type='Machine',
            currency_code='EUR',
            plant=self.plant,
            department=self.department,
        )
        
        self.assertEqual(Equipment.objects.count(), 1)
        created_equipment = Equipment.objects.first()
        self.assertEqual('TestEquipment', created_equipment.description)

