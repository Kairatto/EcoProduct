from rest_framework import generics

from apps.production.models import Production, ProductionShort
from apps.production.serializers import ProductionSerializer, ProductionShortSerializer


class ProductionListView(generics.ListAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductionShortListView(generics.ListAPIView):
    queryset = ProductionShort.objects.all()
    serializer_class = ProductionShortSerializer
