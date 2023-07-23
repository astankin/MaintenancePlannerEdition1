from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import path

from MaintenancePlanner.accounts import views
from MaintenancePlanner.accounts.views import ListUsers, DeleteUser

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='password-reset.html'), name='password-reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='password-reset-done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
    path('list/', ListUsers.as_view(), name='users-list'),
    path('delete/<int:pk>/', DeleteUser.as_view(), name='delete-user'),
]
