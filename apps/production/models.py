from django.db import models
from django.db.models import CharField

from apps.language.models import Language


class Production(models.Model):
    image = models.FileField(upload_to='production_images', verbose_name='Картинка производства')
    title = models.CharField(max_length=5000, verbose_name='Слогон производства')
    description = models.TextField(max_length=5000, verbose_name='Описание производства')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='production')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'


class ProductionShort(models.Model):
    image = models.FileField(upload_to='production_short_images', verbose_name='Картинка производства')
    title = models.CharField(max_length=5000, verbose_name='Слогон производства')
    description = models.TextField(max_length=5000, verbose_name='Описание производства')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='production_short')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Краткая информация производства'
        verbose_name_plural = 'Краткие информации производств'


class ProductionProcess(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    text_1 = models.TextField(max_length=5000, verbose_name='Текст слева сверху')
    text_2 = models.TextField(max_length=5000, verbose_name='Текст справа сверху')
    text_3 = models.TextField(max_length=5000, verbose_name='Текст слева снизу')
    text_4 = models.TextField(max_length=5000, verbose_name='Текст справа снизу')

    fact_title = models.CharField(max_length=5000, verbose_name='Факт заглавная')
    fact_text = models.TextField(max_length=5000, verbose_name='Факт текст')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='production_process')


class ProductionPath(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Слогон пути производства')

    title_1 = models.CharField(max_length=5000, verbose_name='Заглавная_1')
    desc_1 = models.TextField(max_length=5000, verbose_name='Описание_1')
    image_1 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_1')

    title_2 = models.CharField(max_length=5000, verbose_name='Заглавная_2')
    desc_2 = models.TextField(max_length=5000, verbose_name='Описание_2')
    image_2 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_2')

    title_3 = models.CharField(max_length=5000, verbose_name='Заглавная_3')
    desc_3 = models.TextField(max_length=5000, verbose_name='Описание_3')
    image_3 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_3')

    title_4 = models.CharField(max_length=5000, verbose_name='Заглавная_4')
    desc_4 = models.TextField(max_length=5000, verbose_name='Описание_4')
    image_4 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_4')

    title_5 = models.CharField(max_length=5000, verbose_name='Заглавная_5')
    desc_5 = models.TextField(max_length=5000, verbose_name='Описание_5')
    image_5 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_5')

    title_6 = models.CharField(max_length=5000, verbose_name='Заглавная_6')
    desc_6 = models.TextField(max_length=5000, verbose_name='Описание_6')
    image_6 = models.FileField(upload_to='production_path_images', verbose_name='Картинка_6')

    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='production_path')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Путь производства'
        verbose_name_plural = 'Путь производства'
