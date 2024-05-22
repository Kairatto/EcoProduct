from rest_framework import generics


from apps.content.models import Video, LogoCompany
from apps.content.serializers import VideoSerializer, LogoCompanySerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class LogoCompanyListView(generics.ListAPIView):
    queryset = LogoCompany.objects.all()
    serializer_class = LogoCompanySerializer
