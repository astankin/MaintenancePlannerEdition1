from django.contrib import admin

from MaintenancePlanner.plant.models import Department, Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
