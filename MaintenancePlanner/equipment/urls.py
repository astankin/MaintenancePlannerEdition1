from django.urls import path

from MaintenancePlanner.equipment import views
from MaintenancePlanner.equipment.views import CreateEquipment, UpdateEquipment, DeleteEquipment, EquipmentListView

urlpatterns = [
    path('equipment-list/', EquipmentListView.as_view(), name='equipment-list'),
    path('<int:pk>/details/', views.view_equipment, name='view-equipment'),
    path('create/', CreateEquipment.as_view(), name='create-equipment'),
    path('<int:pk>/edit/', UpdateEquipment.as_view(), name='edit-equipment'),
    path('<int:pk>/delete/', DeleteEquipment.as_view(), name='delete-equipment'),
    path('advanced-search/', views.advanced_search_equipment, name='advanced-search-equipment'),
    path('search/', views.search_equipment, name='search-equipment'),
]
