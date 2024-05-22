from django.urls import path

from apps.flavor.views import FlavorListView, FlavorDetailView


urlpatterns = [
    path('list/', FlavorListView.as_view(), name='flavor-list'),
    path('detail/<int:pk>/', FlavorDetailView.as_view(), name='flavor-detail'),
]
