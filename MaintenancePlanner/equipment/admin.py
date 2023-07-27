from django.contrib import admin

from MaintenancePlanner.equipment.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fields = ['description', 'type', 'acquisition_date',
              'acquisition_value', 'year_of_manufacture',
              'manufacturer','model_number', 'part_number',
              'serial_number', 'plant', 'department'
              ]
    list_display = ['description', 'type', 'manufacturer', 'plant', 'department']
    list_filter = ['description', 'type', 'manufacturer', 'plant', 'department']
    ordering = ['plant', 'department']
    search_fields = ['id', 'description', 'type']
