from django.apps import AppConfig


class FlavorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.flavor'

    def ready(self):
        import apps.partners.signals

