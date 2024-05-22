from rest_framework import generics

from apps.flavor.models import Flavor
from apps.flavor.serializers import FlavorSerializer


class FlavorListView(generics.ListAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class FlavorDetailView(generics.RetrieveAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
