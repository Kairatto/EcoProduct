from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.flavor.models import Flavor
from apps.flavor.serializers import FlavorListSerializer


class FlavorFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Flavor
        fields = ['language']


class FlavorListView(generics.ListAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlavorFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class FlavorDetailView(generics.RetrieveAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorListSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
