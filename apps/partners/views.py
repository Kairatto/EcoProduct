from rest_framework import generics

from apps.partners.models import OurPartners, BecomeAPartner
from apps.partners.serializers import OurPartnersSerializer, BecomeAPartnerSerializer


class OurPartnersListView(generics.ListAPIView):
    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerializer


class BecomeAPartnerListView(generics.ListAPIView):
    queryset = BecomeAPartner.objects.all()
    serializer_class = BecomeAPartnerSerializer


class BecomeAPartnerCreateView(generics.CreateAPIView):
    queryset = BecomeAPartner.objects.all()
    serializer_class = BecomeAPartnerSerializer
