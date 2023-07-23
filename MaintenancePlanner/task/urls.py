from django.urls import path

from MaintenancePlanner.task import views
from MaintenancePlanner.task.views import UserTaskList, UserUpdateTask, AllTasksList, UpdateTask

urlpatterns = [
    path('create-task/<int:pk>/', views.create_task, name='create-task'),
    path('task-list/', UserTaskList.as_view(), name='user-task-list'),
    path('user-update-task/<int:pk>/', UserUpdateTask.as_view(), name='user-update-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('all-tasks/', AllTasksList.as_view(), name='all-tasks'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update-task'),
    path('complete/<int:pk>/', views.complete_task, name='complete-task'),
]
