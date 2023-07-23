from django.contrib import admin

from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel, Operation


@admin.register(MaintenancePlanModel)
class MPAdmin(admin.ModelAdmin):
    pass


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass
