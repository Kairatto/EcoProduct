from rest_framework import serializers
from .models import Links, Contacts


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('id', 'title', 'youtube', 'facebook', 'instagram', 'another_1', 'another_2', 'another_3')


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'hotline', 'sales_department', 'marketing_department')
