from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

