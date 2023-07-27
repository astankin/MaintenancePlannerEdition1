from django.contrib import admin

from MaintenancePlanner.service_history.models import ServiceHistory


# Register your models here.
@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    fields = ['created_at', 'equipment', 'technician', 'problem_description', 'solution']
    list_display = ['created_at', 'equipment', 'technician']
    list_filter = ['created_at', 'equipment', 'technician']
    ordering = ['equipment', 'created_at']
    search_fields = ['equipment']
