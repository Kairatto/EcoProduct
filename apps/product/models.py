from django.db import models

from apps.brand.models import Brand
from apps.flavor.models import Flavor


class Volume(models.Model):
    title = models.CharField(max_length=500, verbose_name='Объем продукта')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Объем'
        verbose_name_plural = 'Объемы'


class Product(models.Model):
    image = models.ImageField(upload_to='product_images', verbose_name='Фотография продукта')
    title = models.CharField(max_length=5000, verbose_name='Название продукта', blank=True, null=True)
    volume = models.ForeignKey(to=Volume, on_delete=models.DO_NOTHING, related_name='products')
    flavor = models.ForeignKey(to=Flavor, on_delete=models.DO_NOTHING, related_name='products')
    brand = models.ForeignKey(to=Brand, on_delete=models.DO_NOTHING, related_name='products')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
