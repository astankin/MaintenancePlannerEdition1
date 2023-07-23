from django.urls import path

from MaintenancePlanner.common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
]