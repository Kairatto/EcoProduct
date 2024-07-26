from rest_framework import generics
from django_filters import rest_framework as filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.news.models import News
from apps.news.serializers import NewsSerializer


class NewsFilter(filters.FilterSet):
    specific = filters.CharFilter(field_name="specific")
    language = filters.NumberFilter(field_name="language__id")

    class Meta:
        model = News
        fields = ['language', 'specific']


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFilter

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
