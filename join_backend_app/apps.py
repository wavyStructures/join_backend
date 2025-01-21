from django.apps import AppConfig


class JoinBackendAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_backend_app'


    def ready(self):
        import join_backend_app.signals  
        