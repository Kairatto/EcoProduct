from rest_framework import serializers
from .models import Vacancy, DefaultVacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'required_work_experience', 'schedule', 'responsibilities',
                  'requirements', 'conditions', 'address', 'link', 'date', 'language',)


class DefaultVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultVacancy
        fields = ('id', 'title', 'link')
