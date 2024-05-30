from django.db import models

from apps.language.models import Language


class OurPartners(models.Model):
    image = models.ImageField(upload_to='our_partners_images', verbose_name='Лого партнера')
    title = models.CharField(max_length=5000, verbose_name='Название партнера')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Наши Партнеры'


class BecomeAPartner(models.Model):
    name = models.CharField(max_length=5000, verbose_name='Имя')
    country = models.CharField(max_length=5000, verbose_name='Страна')
    email = models.CharField(max_length=5000, verbose_name='email')
    description = models.TextField(max_length=5000, verbose_name='Кратко опишите идею сотрудничества')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='become_a_partner')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Заявка на партнерство'
        verbose_name_plural = 'Заявки на партнерство'
