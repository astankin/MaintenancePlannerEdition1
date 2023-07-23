from django.urls import path

from MaintenancePlanner.plant.views import PlantCreateView, DepartmentCreateView, PlantListView, PlantDeleteView, \
    PlantUpdateView, DepartmentListVie, DepartmentDeleteView, DepartmentUpdateView

urlpatterns = [
    path('create/', PlantCreateView.as_view(), name='create-plant'),
    path('list/', PlantListView.as_view(), name='plants-list'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='delete-plant'),
    path('update/<int:pk>/', PlantUpdateView.as_view(), name='update-plant'),
    path('department/create/', DepartmentCreateView.as_view(), name='create-department'),
    path('department-list/', DepartmentListVie.as_view(), name='department-list'),
    path('delete/department/<int:pk>/', DepartmentDeleteView.as_view(), name='delete-department'),
    path('update/department/<int:pk>/', DepartmentUpdateView.as_view(), name='update-department'),
]
