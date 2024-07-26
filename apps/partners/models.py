from django.db import models
from django.db.models import CharField


class OurPartners(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Название партнера')
    image = models.FileField(upload_to='our_partners_images', verbose_name='Лого партнера')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Наши Партнеры'


class BecomeAPartner(models.Model):
    name = models.CharField(max_length=5000, verbose_name='Имя')
    email = models.CharField(max_length=5000, verbose_name='email')
    country = models.CharField(max_length=5000, verbose_name='Страна')
    description = models.TextField(max_length=5000, verbose_name='Кратко опишите идею сотрудничества')

    def __str__(self) -> CharField:
        return self.name

    class Meta:
        verbose_name = 'Заявка на партнерство'
        verbose_name_plural = 'Заявки на партнерство'
