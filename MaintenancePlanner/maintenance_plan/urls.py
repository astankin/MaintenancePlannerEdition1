from django.urls import path

from MaintenancePlanner.maintenance_plan import views
from MaintenancePlanner.maintenance_plan.views import OperationDetail, UpdateOperation, DeleteMP, CreateMPView

urlpatterns = [
    path('create/<int:pk>/', views.create_mp, name='create-mp'),
    path('details/<int:pk>/', views.mp_details, name='mp-details'),
    path('delete/<int:pk>/', DeleteMP.as_view(), name='mp-delete'),
    path('create-operation/<int:pk>/', views.create_operation, name='create-operation'),
    path('operation-details/<int:pk>/', OperationDetail.as_view(), name='operation-details'),
    path('operation-update/<int:pk>/', UpdateOperation.as_view(), name='operation-update'),
    path('operation-delete/<int:pk>/', views.delete_operation, name='delete-operation'),
    # path('list/', ListMp.as_view(), name='mp-list'),
    path('createMP/', CreateMPView.as_view(), name='create-maintenance-plan'),

]
