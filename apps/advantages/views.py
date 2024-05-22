from rest_framework import generics

from apps.advantages.models import Advantages
from apps.advantages.serializers import AdvantagesSerializer


class AdvantagesListView(generics.ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer
