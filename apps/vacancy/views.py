from rest_framework import generics

from apps.vacancy.models import Vacancy, DefaultVacancy
from apps.vacancy.serializers import VacancySerializer, DefaultVacancySerializer


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class DefaultVacancyListView(generics.ListAPIView):
    queryset = DefaultVacancy.objects.all()
    serializer_class = DefaultVacancySerializer
