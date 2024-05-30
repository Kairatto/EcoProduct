from django.db import models

from apps.language.models import Language


class Advantages(models.Model):
    image = models.ImageField(upload_to='advantages_images', verbose_name='Картинка Преимущества')
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='advantages')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'
