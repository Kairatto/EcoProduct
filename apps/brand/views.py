from rest_framework import generics


from apps.brand.models import Brand
from apps.brand.serializers import BrandListSerializer


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
