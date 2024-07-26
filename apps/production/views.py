from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.production.models import Production, ProductionShort, ProductionProcess, ProductionPath
from apps.production.serializers import (ProductionSerializer, ProductionShortSerializer, ProductionProcessSerializer,
                                         ProductionPathSerializer)


class ProductionFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Production
        fields = ['language']


class ProductionListView(generics.ListAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductionFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductionShortFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = ProductionShort
        fields = ['language']


class ProductionShortListView(generics.ListAPIView):
    queryset = ProductionShort.objects.all()
    serializer_class = ProductionShortSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductionShortFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductionProcessFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = ProductionProcess
        fields = ['language']


class ProductionProcessListView(generics.ListAPIView):
    queryset = ProductionProcess.objects.all()
    serializer_class = ProductionProcessSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductionProcessFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductionPathFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = ProductionPath
        fields = ['language']


class ProductionPathListView(generics.ListAPIView):
    queryset = ProductionPath.objects.all()
    serializer_class = ProductionPathSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductionPathFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
