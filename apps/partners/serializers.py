from rest_framework import serializers
from .models import OurPartners, BecomeAPartner


class OurPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartners
        fields = ('id', 'image', 'title', )


class BecomeAPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeAPartner
        fields = ('id', 'name', 'country', 'email', 'description', 'language')
