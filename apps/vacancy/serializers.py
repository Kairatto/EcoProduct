from rest_framework import serializers
from .models import Vacancy, DefaultVacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'link', 'date',)


class DefaultVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultVacancy
        fields = ('id', 'title', 'link')
