from django.db import models


# Create your models here.
class Plant(models.Model):
    name = models.CharField(
        max_length=30,
    )
    country = models.CharField(
        max_length=30,
    )
    city = models.CharField(
        max_length=30,
    )
    address = models.CharField(
        max_length=50,
    )
    cost_center = models.CharField(
        max_length=10,
        verbose_name='Cost Center'
    )

    def __str__(self):
        return f'{self.cost_center}'


class Department(models.Model):
    name = models.CharField(
        max_length=30,
    )
    plant = models.ForeignKey(
        to=Plant,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
