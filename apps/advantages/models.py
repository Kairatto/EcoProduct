from django.db import models
from django.db.models import CharField

from apps.language.models import Language


class Advantages(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    image = models.FileField(upload_to='advantages_images', verbose_name='Картинка Преимущества')
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, related_name='advantages', blank=True, null=True)

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'
