from django.db import models


class ProductionShort(models.Model):
    image = models.ImageField(upload_to='production_short_images', verbose_name='Картинка производства')
    title = models.CharField(max_length=500, verbose_name='Слогон производства')
    description = models.TextField(max_length=500, verbose_name='Описание производства')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Краткая информация производства'
        verbose_name_plural = 'Краткие информации производств'


class Production(models.Model):
    image = models.ImageField(upload_to='production_images', verbose_name='Картинка производства')
    title = models.CharField(max_length=500, verbose_name='Слогон производства')
    description = models.TextField(max_length=500, verbose_name='Описание производства')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Информация производства'
        verbose_name_plural = 'Информации производств'
