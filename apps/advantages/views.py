from rest_framework import generics
from django_filters import rest_framework as filters

from apps.advantages.models import Advantages
from apps.advantages.serializers import AdvantagesSerializer


class AdvantagesFilter(filters.FilterSet):
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = Advantages
        fields = ['language']


class AdvantagesListView(generics.ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvantagesFilter
