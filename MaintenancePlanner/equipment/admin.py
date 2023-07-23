from django.contrib import admin

from MaintenancePlanner.equipment.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
