from rest_framework import generics
from django_filters import rest_framework as filters

from apps.vacancy.models import Vacancy, DefaultVacancy
from apps.vacancy.serializers import VacancySerializer, DefaultVacancySerializer


class VacancyFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Vacancy
        fields = ['language']


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter


class VacancyDetailView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class DefaultVacancyListView(generics.ListAPIView):
    queryset = DefaultVacancy.objects.all()
    serializer_class = DefaultVacancySerializer
