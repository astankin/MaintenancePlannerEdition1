from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from PIL import Image

from MaintenancePlanner.accounts.validators import user_name_validator


class AppUser(AbstractUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(4),
        ],
        unique=True,
    )
    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            user_name_validator,
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            user_name_validator,
        ]
    )
    email = models.EmailField(unique=True)

    class Role(models.TextChoices):
        MANAGER = "MANAGER", 'Manager'
        SUPERVISOR = "SUPERVISOR", 'Supervisor'
        OPERATOR = "OPERATOR", 'Operator'

    role = models.CharField(max_length=50, choices=Role.choices)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    image = models.ImageField(
        default='images/default.jpg',
        null=True,
        blank=True,
        upload_to='images/'
    )

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'



