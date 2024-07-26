from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.brand_info.models import BrandInfo, BrandHistory
from apps.brand_info.serializers import BrandInfoSerializer, BrandHistorySerializer


class BrandInfoFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = BrandInfo
        fields = ['language']


class BrandInfoListView(generics.ListAPIView):
    queryset = BrandInfo.objects.all()
    serializer_class = BrandInfoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandInfoFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BrandHistoryFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = BrandHistory
        fields = ['language']


class BrandHistoryListView(generics.ListAPIView):
    queryset = BrandHistory.objects.all()
    serializer_class = BrandHistorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandHistoryFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
