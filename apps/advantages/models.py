from django.db import models


class Advantages(models.Model):
    image = models.ImageField(upload_to='advantages_images', verbose_name='Картинка Преимущества')
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'
