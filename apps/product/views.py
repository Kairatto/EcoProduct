from rest_framework import generics
from django_filters import rest_framework as filters

from apps.brand.models import Brand
from apps.product.models import Product, Category

from apps.product.serializers import ProductSerializer, CategorySerializer, BrandSerializer


class BrandtFilter(filters.FilterSet):
    brand = filters.NumberFilter(field_name="id")
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Brand
        fields = ['brand', 'language']


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandtFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

