from django.db import models

from apps.language.models import Language


class Brand(models.Model):
    tagline = models.CharField(max_length=5000, verbose_name='Слоган', blank=True, null=True)
    file = models.FileField(upload_to='brand_file', verbose_name='Файл', blank=True, null=True)
    title = models.CharField(max_length=5000, verbose_name='Название бренда', blank=True, null=True)
    flavor_bg = models.FileField(upload_to='flavor_bg', verbose_name='Фон вкуса', blank=True, null=True)
    description = models.TextField(max_length=5000, verbose_name='Описание бренда', blank=True, null=True)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, related_name='brand', blank=True, null=True)
    background = models.FileField(upload_to='background_images', verbose_name='Фотография фона', blank=True, null=True)
    image_circle = models.FileField(upload_to='brand_circle_images', verbose_name='Фотография бренда', blank=True, null=True)
    image_main = models.FileField(upload_to='brand_main_images', verbose_name='Главная фотография бренда', blank=True, null=True)
    image_logo = models.FileField(upload_to='brand_logo_images', verbose_name='Фотография логотипа бренда', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.tagline}"

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
