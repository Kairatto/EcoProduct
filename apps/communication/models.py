from django.db import models


class Links(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Название', blank=True, null=True)
    youtube = models.CharField(max_length=5000, verbose_name='Ссылка на ютуб', blank=True, null=True)
    facebook = models.CharField(max_length=5000, verbose_name='Ссылка на фейсбук', blank=True, null=True)
    instagram = models.CharField(max_length=5000, verbose_name='Ссылка на инстаграмм', blank=True, null=True)
    another_1 = models.CharField(max_length=5000, verbose_name='Ссылка на другую социальную сеть 1', blank=True, null=True)
    another_2 = models.CharField(max_length=5000, verbose_name='Ссылка на другую социальную сеть 2', blank=True, null=True)
    another_3 = models.CharField(max_length=5000, verbose_name='Ссылка на другую социальную сеть 3', blank=True, null=True)

    class Meta:
        verbose_name = 'Ссылка на другую платформу'
        verbose_name_plural = 'Ссылки на другуие платформы'


class Contacts(models.Model):
    hotline = models.CharField(max_length=5000, verbose_name='Горячая линия', blank=True, null=True)
    sales_department = models.CharField(max_length=5000, verbose_name='Отдел продаж', blank=True, null=True)
    marketing_department = models.CharField(max_length=5000, verbose_name='Отдел маркетинга', blank=True, null=True)

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
