from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.communication.models import Links, Contacts
from apps.communication.serializers import LinksSerializer, ContactsSerializer


class LinksListView(generics.ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ContactsListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
