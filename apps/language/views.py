from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.language.models import Language
from apps.language.serializers import LanguageSerializer


class LanguageListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LanguageDetailView(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

