from rest_framework import generics
from django_filters import rest_framework as filters

from apps.brand.models import Brand

from apps.product.serializers import BrandSerializer


class BrandFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="title")
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Brand
        fields = ['brand', 'language']


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

