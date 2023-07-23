from django.contrib import admin

from MaintenancePlanner.service_history.models import ServiceHistory


# Register your models here.
@admin.register(ServiceHistory)
class DepartmentAdmin(admin.ModelAdmin):
    pass
