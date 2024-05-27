from rest_framework import generics


from apps.brand.models import Brand
from apps.brand.serializers import BrandListSerializer, AnotherProductsSerializer


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class AnotherProductsListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = AnotherProductsSerializer


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
