from rest_framework import generics
from django_filters import rest_framework as filters

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


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
