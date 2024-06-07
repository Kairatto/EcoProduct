from django.db import models

from apps.language.models import Language


class BrandInfo(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Слогон компании')
    description = models.TextField(max_length=5000, verbose_name='Подробнее о компании')
    title_1 = models.CharField(max_length=5000, verbose_name='1 загланая', null=True)
    desc_1 = models.TextField(max_length=5000, verbose_name='1 ячейка')
    title_2 = models.CharField(max_length=5000, verbose_name='2 загланая', null=True)
    desc_2 = models.TextField(max_length=5000, verbose_name='2 ячейка')
    title_3 = models.CharField(max_length=5000, verbose_name='3 загланая', null=True)
    desc_3 = models.TextField(max_length=5000, verbose_name='3 ячейка')
    title_4 = models.CharField(max_length=5000, verbose_name='4 загланая', null=True)
    desc_4 = models.TextField(max_length=5000, verbose_name='4 ячейка')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='brand_info')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компаний'


class BrandHistory(models.Model):
    image = models.ImageField(upload_to='logo_images', verbose_name='Логотип для истории бренда')
    year = models.CharField(max_length=5000, verbose_name='Год истории бренда')
    description = models.TextField(max_length=5000, verbose_name='Описание истории бренда')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='brand_history')

    def __str__(self) -> str:
        return self.year

    class Meta:
        verbose_name = 'История бренда'
        verbose_name_plural = 'Истории брендов'
