from django.apps import AppConfig


class BrandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.brand'

    def ready(self):
        import apps.partners.signals

