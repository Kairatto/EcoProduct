from rest_framework import generics

from apps.communication.models import Links, Contacts
from apps.communication.serializers import LinksSerializer, ContactsSerializer


class LinksListView(generics.ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class ContactsListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
