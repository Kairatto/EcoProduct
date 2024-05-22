from django.db import models


class Brand(models.Model):
    image_logo = models.ImageField(upload_to='brand_logo_images', verbose_name='Фотография логотипа бренда')
    image_circle = models.ImageField(upload_to='brand_circle_images', verbose_name='Фотография бренда')
    title = models.CharField(max_length=5000, verbose_name='Название бренда')
    description = models.TextField(max_length=5000, verbose_name='Описание бренда')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
