from django.db import models
from django.db.models import CharField

from apps.language.models import Language


class News(models.Model):
    image = models.FileField(upload_to='news_images', verbose_name='Фотография')
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    specific = models.CharField(max_length=5000, verbose_name='Определите новость, для разных языков', null=True)
    description = models.TextField(max_length=5000, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата публикации')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='news')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
