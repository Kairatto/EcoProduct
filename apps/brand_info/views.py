from rest_framework import generics


from apps.brand_info.models import BrandInfo, BrandHistory
from apps.brand_info.serializers import BrandInfoSerializer, BrandHistorySerializer


class BrandInfoListView(generics.ListAPIView):
    queryset = BrandInfo.objects.all()
    serializer_class = BrandInfoSerializer


class BrandHistoryListView(generics.ListAPIView):
    queryset = BrandHistory.objects.all()
    serializer_class = BrandHistorySerializer
