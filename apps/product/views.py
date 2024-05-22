from rest_framework import generics

from apps.product.models import Product, Volume

from apps.product.serializers import ProductSerializer, VolumeSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VolumeListView(generics.ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer


class VolumeDetailView(generics.RetrieveAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
