from django.db import models
from django.db.models import CharField


class LogoCompany(models.Model):
    image = models.FileField(upload_to='logo_company_images', verbose_name='Фотография логотипа компании')
    title = models.CharField(max_length=5000, verbose_name='Название компании')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Логотип компании'
        verbose_name_plural = 'Логотипы компаний'


class Video(models.Model):
    video = models.FileField(upload_to='video', verbose_name='Видео')
    title = models.CharField(max_length=5000, verbose_name='Название Видео')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео файлы'
