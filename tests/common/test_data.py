from django.contrib.auth import get_user_model

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel
from MaintenancePlanner.plant.models import Plant, Department
from MaintenancePlanner.service_history.models import ServiceHistory
from MaintenancePlanner.task.models import Task

AppUser = get_user_model()


def create_user(role):
    return AppUser.objects.create_user(
        username='astankin',
        password='password123',
        email='astankin@abv.bg',
        role=role,
    )


def create_mp():
    return MaintenancePlanModel.objects.create(
        name='TestMP',
        equipment=create_equipment()
    )


def create_task():
    return Task.objects.create(
        technician=create_user('OPERATOR'),
        equipment=create_equipment(),
        title='TestTask'

    )


def create_service_history():
    return ServiceHistory.objects.create(
        technician=create_user('OPERATOR'),
        problem_description='Some Description',
        solution='Some Solution',
        equipment=create_equipment()
    )


def create_plant():
    return Plant.objects.create(
        name='TestPlant',
        country='Bulgaria',
        city='Plovdiv',
        address='Address',
        cost_center='BG20',
    )


def create_department():
    return Department.objects.create(
        name='TestDepartment',
        plant=create_plant()
    )


def create_equipment():
    return Equipment.objects.create(
        description='TestEquipment',
        type='Machine',
        currency_code='EUR',
        plant=create_plant(),
        department=create_department(),
    )
