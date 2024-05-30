from rest_framework import generics

from apps.production.models import ProductionShort
from apps.production.serializers import ProductionShortSerializer


class ProductionShortListView(generics.ListAPIView):
    queryset = ProductionShort.objects.all()
    serializer_class = ProductionShortSerializer
