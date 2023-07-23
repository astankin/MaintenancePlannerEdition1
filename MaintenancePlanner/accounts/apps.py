from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MaintenancePlanner.accounts'

    def ready(self):
        import MaintenancePlanner.accounts.signals
