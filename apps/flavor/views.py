from rest_framework import generics
from django_filters import rest_framework as filters

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


class FlavorDetailView(generics.RetrieveAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorListSerializer
