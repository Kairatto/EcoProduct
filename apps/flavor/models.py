from django.db import models

from apps.language.models import Language


class Flavor(models.Model):
    image = models.FileField(upload_to='flavor_images', verbose_name='Фотография вкуса')
    title = models.CharField(max_length=5000, verbose_name='Название вкуса')
    description = models.TextField(max_length=5000, verbose_name='Описание вкуса')
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='flavor')

    def __str__(self) -> str:
        return f"{self.title} - {self.description[:50]}"

    class Meta:
        verbose_name = 'Вкус'
        verbose_name_plural = 'Вкусы'
