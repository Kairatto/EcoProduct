from django.db import models

from apps.language.models import Language


class ProductionShort(models.Model):
    image = models.ImageField(upload_to='production_short_images', verbose_name='Картинка производства')
    title = models.CharField(max_length=5000, verbose_name='Слогон производства')
    description = models.TextField(max_length=5000, verbose_name='Описание производства')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='production_short')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Краткая информация производства'
        verbose_name_plural = 'Краткие информации производств'
