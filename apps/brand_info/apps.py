from django.apps import AppConfig


class BrandInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.brand_info'

    def ready(self):
        import apps.partners.signals

