from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from MaintenancePlanner.accounts.forms import UserRegisterForm
from MaintenancePlanner.accounts.models import Profile


UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )
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


# admin.site.unregister(Group)
