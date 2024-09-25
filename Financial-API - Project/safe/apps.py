from django.apps import AppConfig


class SafeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'safe'
