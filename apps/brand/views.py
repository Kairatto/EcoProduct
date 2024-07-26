from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.brand.models import Brand
from apps.brand.serializers import BrandListSerializer


class BrandListFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Brand
        fields = ['language']


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandListFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
