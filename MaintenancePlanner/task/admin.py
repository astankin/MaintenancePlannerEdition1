from django.contrib import admin

from MaintenancePlanner.task.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['technician', 'equipment', 'title', 'description', 'created_on']
    list_display = ['technician', 'equipment', 'title', 'complete']
    list_filter = ['technician', 'equipment', 'technician']
    ordering = ['technician', 'equipment']
    search_fields = ['title']


