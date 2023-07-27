from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from MaintenancePlanner.equipment.models import Equipment

UserModel = get_user_model()


class ServiceHistory(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    equipment = models.ForeignKey(
        to=Equipment,
        on_delete=models.CASCADE,
    )
    technician = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    problem_description = models.TextField()
    solution = models.TextField()
