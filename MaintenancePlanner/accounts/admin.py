from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from MaintenancePlanner.accounts.models import Profile

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'email', 'role']
    list_display = ['username', 'first_name', 'last_name', 'role', 'date_joined']
    list_filter = ['username', 'date_joined', 'role']
    ordering = ['date_joined']
    search_fields = ['username']


@admin.register(Profile)
class ProfileModelAdmin(ModelAdmin):
    fields = ['user', 'image']
    list_display = ['user', 'image']
    list_filter = ['user']
    ordering = ['user']
    search_fields = ['user']


admin.site.unregister(Group)
