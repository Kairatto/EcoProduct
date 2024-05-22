from django.urls import path

from apps.advantages.views import AdvantagesListView


urlpatterns = [
    path('list/', AdvantagesListView.as_view(), name='advantages-list'),
    ]
