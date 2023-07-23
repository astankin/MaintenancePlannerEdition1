from django.urls import path

from MaintenancePlanner.service_history import views
from MaintenancePlanner.service_history.views import CreateServiceReport, ReportDetailView, ReportUpdateView

urlpatterns = [
    path('<int:pk>/', views.service_history, name='service-history'),
    path('create/', CreateServiceReport.as_view(), name='create-service-report'),
    path('report/', ReportDetailView.as_view(), name='view-report'),
    path('report/update/<int:pk>/', ReportUpdateView.as_view(), name='update-report'),

]
