from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.vacancy.models import Vacancy, DefaultVacancy
from apps.vacancy.serializers import VacancySerializer, DefaultVacancySerializer


class VacancyFilter(filters.FilterSet):
    specific = filters.CharFilter(field_name="specific")
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Vacancy
        fields = ['language', 'specific']


class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class VacancyDetailView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DefaultVacancyListView(generics.ListAPIView):
    queryset = DefaultVacancy.objects.all()
    serializer_class = DefaultVacancySerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
