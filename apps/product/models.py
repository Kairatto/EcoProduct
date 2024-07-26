from django.db import models
from django.db.models import CharField

from apps.brand.models import Brand
from apps.flavor.models import Flavor
from apps.language.models import Language


class Category(models.Model):
    title = models.CharField(max_length=500, verbose_name='Объем продукта')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Объем'
        verbose_name_plural = 'Объемы'


class Product(models.Model):
    image = models.FileField(upload_to='product_images', verbose_name='Фотография продукта')
    title = models.CharField(max_length=5000, verbose_name='Название продукта', blank=True, null=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    flavor = models.ForeignKey(to=Flavor, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
