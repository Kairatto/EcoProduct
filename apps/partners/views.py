from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.partners.models import OurPartners, BecomeAPartner
from apps.partners.serializers import OurPartnersSerializer, BecomeAPartnerSerializer


class OurPartnersListView(generics.ListAPIView):
    queryset = OurPartners.objects.all()
    serializer_class = OurPartnersSerializer

    @method_decorator(cache_page(60 * 1440))  # 1 день
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BecomeAPartnerListView(generics.ListAPIView):
    queryset = BecomeAPartner.objects.all()
    serializer_class = BecomeAPartnerSerializer


class BecomeAPartnerCreateView(generics.CreateAPIView):
    queryset = BecomeAPartner.objects.all()
    serializer_class = BecomeAPartnerSerializer
