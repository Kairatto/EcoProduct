from django.db import models
from django.db.models import CharField

from apps.language.models import Language


class News(models.Model):
    date = models.DateField(verbose_name='Дата публикации')
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    image = models.FileField(upload_to='news_images', verbose_name='Фотография')
    specific = models.CharField(max_length=5000, verbose_name='Определите новость, для разных языков', null=True)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, related_name='news', blank=True, null=True)

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
