from django.apps import AppConfig


class VacancyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.vacancy'

    def ready(self):
        import apps.partners.signals

