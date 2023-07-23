from django.core.exceptions import ValidationError
from django.test import TestCase
from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.equipment.validators import equipment_name_validator
from tests.common.test_data import create_plant, create_department, create_equipment


class EquipmentCreationModel(TestCase):
    def setUp(self):
        self.plant = create_plant()
        self.department = create_department()

    def test_equipment_creation_with_valid_data(self):
        equipment = create_equipment()
        self.assertEqual(equipment.description, 'TestEquipment')
        self.assertEqual(equipment.type, 'Machine')
        self.assertEqual(equipment.plant.name, 'TestPlant')
        self.assertEqual(equipment.department.name, 'TestDepartment')

    def test_equipment_creation_with_invalid_data(self):
        equipment = Equipment.objects.create(
                description='TestEquipment@',
                type='Machine',
                plant=self.plant,
                department=self.department,
            )
        with self.assertRaises(ValidationError) as context:
            equipment_name_validator(equipment.description)
        message = 'Ensure this value contains only letters, numbers, and underscore.'
        self.assertEqual(message, str(context.exception.message))
