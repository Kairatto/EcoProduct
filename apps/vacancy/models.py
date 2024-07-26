from django.db import models
from django.db.models import CharField

from apps.language.models import Language


class Vacancy(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заглавная')
    required_work_experience = models.TextField(max_length=5000, verbose_name='Требуемый опыт работы', blank=True, null=True)
    schedule = models.TextField(max_length=5000, verbose_name='График', blank=True, null=True)
    responsibilities = models.TextField(max_length=5000, verbose_name='Обязанности', blank=True, null=True)
    requirements = models.TextField(max_length=5000, verbose_name='Требования', blank=True, null=True)
    conditions = models.TextField(max_length=5000, verbose_name='Условия', blank=True, null=True)
    address = models.TextField(max_length=5000, verbose_name='Адрес', blank=True, null=True)
    link = models.CharField(max_length=5000, verbose_name='Ссылка', blank=True, null=True)
    date = models.DateField(verbose_name='Дата публикации')
    specific = models.CharField(max_length=5000, verbose_name='Определите вакансию, для разных языков', null=True)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, related_name='vacancy', blank=True, null=True)

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class DefaultVacancy(models.Model):
    title = models.CharField(max_length=5000, verbose_name='Заглавная', blank=True)
    link = models.CharField(max_length=5000, verbose_name='Ссылка')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = 'Ссылка по умолчанию'
        verbose_name_plural = 'Ссылка по умолчанию'
