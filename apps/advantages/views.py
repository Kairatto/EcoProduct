from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

