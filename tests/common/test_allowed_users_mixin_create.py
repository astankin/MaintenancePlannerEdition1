from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

AppUser = get_user_model()


class AllowedUsersMixinTest(TestCase):
    def setUp(self):
        self.manager_user = AppUser.objects.create_user(username='manager', password='password123')
        self.manager_user.role = 'MANAGER'
        self.manager_user.save()

        self.supervisor_user = AppUser.objects.create_user(
            username='supervisor',
            email='supervisor@abv.bg',
            password='password123',
        )
        self.supervisor_user.role = 'SUPERVISOR'
        self.supervisor_user.save()

        self.operator_user = AppUser.objects.create_user(
            username='operator',
            email='operator@abv.bg',
            password='password123'
        )
        self.operator_user.role = 'OPERATOR'
        self.operator_user.save()

    def test_allowed_users_can_access_plant_create_view(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('create-plant'))
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_plant_create_view(self):
        self.client.login(username='operator', password='password123')
        response = self.client.get(reverse('create-plant'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         reverse('home-page'))

    def test_allowed_users_can_access_department_create_view(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('create-department'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='supervisor', password='password123')
        response = self.client.get(reverse('create-department'))
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_department_create_view(self):
        self.client.login(username='operator', password='password123')
        response = self.client.get(reverse('create-department'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         reverse('home-page'))

    def test_allowed_users_can_access_task_create_view(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('create-service-report'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='supervisor', password='password123')
        response = self.client.get(reverse('create-service-report'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='operator', password='password123')
        response = self.client.get(reverse('create-service-report'))
        self.assertEqual(response.status_code, 200)

    def test_allowed_users_can_access_create_equipment_view(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('create-equipment'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='supervisor', password='password123')
        response = self.client.get(reverse('create-equipment'))
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_create_equipment_view(self):
        self.client.login(username='operator', password='password123')
        response = self.client.get(reverse('create-equipment'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         reverse('home-page'))

    def test_allowed_users_can_access_create_mp_view(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('create-maintenance-plan'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='supervisor', password='password123')
        response = self.client.get(reverse('create-maintenance-plan'))
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_create_mp_view(self):
        self.client.login(username='operator', password='password123')
        response = self.client.get(reverse('create-maintenance-plan'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         reverse('home-page'))
