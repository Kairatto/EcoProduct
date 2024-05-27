from rest_framework import generics
from django_filters import rest_framework as filters

from apps.brand.models import Brand
from apps.product.models import Product, Category

from apps.product.serializers import ProductSerializer, CategorySerializer, BrandSerializer


class ProductFilter(filters.FilterSet):
    brand = filters.NumberFilter(field_name="brand__id")

    class Meta:
        model = Product
        fields = ['brand']


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
