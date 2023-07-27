from django.contrib import admin

from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel, Operation


@admin.register(MaintenancePlanModel)
class MPAdmin(admin.ModelAdmin):
    fields = ['name', 'equipment']
    list_display = ['name', 'equipment']
    list_filter = ['name']
    ordering = ['equipment']
    search_fields = ['id', 'name']


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'maintenance_plan']
    list_display = ['title', 'maintenance_plan']
    list_filter = ['title', 'maintenance_plan']
    ordering = ['title']
    search_fields = ['id']
