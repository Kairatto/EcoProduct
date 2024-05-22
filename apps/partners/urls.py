from django.urls import path

from apps.partners.views import OurPartnersListView, BecomeAPartnerListView, BecomeAPartnerCreateView

urlpatterns = [
    path('our_partners/list/', OurPartnersListView.as_view(), name='our_partners-list'),
    path('become_a_partner/list/', BecomeAPartnerListView.as_view(), name='become_a_partner-list'),
    path('become_a_partner/create/', BecomeAPartnerCreateView.as_view(), name='become_a_partner-create'),
    ]
