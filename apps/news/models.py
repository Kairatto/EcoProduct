from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news_images', verbose_name='Фотография')
    title = models.CharField(max_length=5000, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата публикации')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
