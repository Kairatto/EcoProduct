from django.db import models
from django.db.models import CharField


class Language(models.Model):
    title = models.CharField(max_length=500, verbose_name='Язык')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
