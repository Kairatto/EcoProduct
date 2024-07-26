from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


from apps.content.models import Video, LogoCompany
from apps.content.serializers import VideoSerializer, LogoCompanySerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LogoCompanyListView(generics.ListAPIView):
    queryset = LogoCompany.objects.all()
    serializer_class = LogoCompanySerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
