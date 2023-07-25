from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from MaintenancePlanner.plant.models import Plant, Department

AppUser = get_user_model()


class AllowedUsersMixinTest(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(name='Test Plant')
        self.department = Department.objects.create(name='Test Department', plant=self.plant)
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

    def test_allowed_users_can_access_plant_update_view(self):
        self.client.login(username='manager', password='password123')
        url = reverse('update-plant', kwargs={'pk': self.plant.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_plant_update_view(self):
        self.client.login(username='operator', password='password123')
        url = reverse('update-plant', kwargs={'pk': self.plant.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home-page'))

        self.client.login(username='supervisor', password='password123')
        url = reverse('update-plant', kwargs={'pk': self.plant.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home-page'))

    def test_allowed_users_can_access_department_update_view(self):
        self.client.login(username='manager', password='password123')
        url = reverse('update-department', kwargs={'pk': self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.login(username='supervisor', password='password123')
        url = reverse('update-department', kwargs={'pk': self.department.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_disallowed_users_can_not_access_department_update_view(self):
        self.client.login(username='operator', password='password123')
        url = reverse('update-department', kwargs={'pk': self.department.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home-page'))
