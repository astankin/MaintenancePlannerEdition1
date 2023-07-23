from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from MaintenancePlanner.accounts.models import Profile

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(ModelAdmin):
    pass


@admin.register(Profile)
class ProfileModelAdmin(ModelAdmin):
    pass

