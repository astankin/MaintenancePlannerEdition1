import datetime
from django.db import models

from MaintenancePlanner.equipment.validators import equipment_name_validator
from MaintenancePlanner.plant.models import Department, Plant

TYPE_OF_EQUIPMENT = [
    ('Machine', 'Machine'),
    ('Measuring tool', 'Measuring tool'),
    ('Hand power tool', 'Hand power tool'),
]

# Create your models here.

CURRENCY_CHOICES = [
    ('EUR', 'EUR'),
    ('BGN', 'BGN'),
    ('USD', 'USD'),
]


class Equipment(models.Model):
    description = models.CharField(
        max_length=50,
        validators=[equipment_name_validator],
    )
    type = models.CharField(
        max_length=30,
        choices=TYPE_OF_EQUIPMENT
    )
    acquisition_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Acquisition Date',
    )
    acquisition_value = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Acquisition Value',
    )
    currency_code = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default='EUR',
    )
    year_of_manufacture = models.PositiveIntegerField(
        verbose_name='Year of Manufacture',
        null=True,
        blank=True,
    )

    manufacturer = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    model_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Model Number'
    )
    part_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Manufacturer Part Number',
    )
    serial_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Manufacturer Serial Number',
    )
    plant = models.ForeignKey(
        to=Plant,
        on_delete=models.CASCADE)
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.description
