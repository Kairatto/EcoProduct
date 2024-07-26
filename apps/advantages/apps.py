from django.apps import AppConfig


class AdvantagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.advantages'

    def ready(self):
        import apps.partners.signals
