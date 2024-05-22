from django.urls import path

from apps.communication.views import LinksListView, ContactsListView


urlpatterns = [
    path('links/list/', LinksListView.as_view(), name='links-list'),
    path('contacts/list/', ContactsListView.as_view(), name='contacts-list'),
    ]
