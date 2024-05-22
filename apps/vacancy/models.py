from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заглавная')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    link = models.CharField(max_length=5000, verbose_name='Ссылка')
    date = models.DateField(verbose_name='Дата публикации')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class DefaultVacancy(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Заглавная', blank=True)
    link = models.CharField(max_length=5000, verbose_name='Ссылка')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Ссылка по умолчанию'
        verbose_name_plural = 'Ссылка по умолчанию'
