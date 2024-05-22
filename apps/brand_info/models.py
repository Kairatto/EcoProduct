from django.db import models


class BrandInfo(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Слогон компании')
    description = models.TextField(max_length=5000, verbose_name='Подробнее о компании')
    desc_1 = models.TextField(max_length=5000, verbose_name='1 ячейка')
    desc_2 = models.TextField(max_length=5000, verbose_name='2 ячейка')
    desc_3 = models.TextField(max_length=5000, verbose_name='3 ячейка')
    desc_4 = models.TextField(max_length=5000, verbose_name='4 ячейка')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компаний'


class BrandHistory(models.Model):
    image = models.ImageField(upload_to='logo_images', verbose_name='Логотип для истории бренда')
    year = models.CharField(max_length=5000, verbose_name='Год истории бренда')
    description = models.TextField(max_length=5000, verbose_name='Описание истории бренда')

    def __str__(self) -> str:
        return self.year

    class Meta:
        verbose_name = 'История бренда'
        verbose_name_plural = 'Истории брендов'
