from django.contrib.auth import get_user_model
from django.db import models

from MaintenancePlanner.equipment.models import Equipment

UserModel = get_user_model()


class Task(models.Model):
    technician = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    equipment = models.ForeignKey(
        to=Equipment,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
