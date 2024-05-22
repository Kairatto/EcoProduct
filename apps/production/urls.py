from django.urls import path

from apps.production.views import ProductionListView, ProductionShortListView


urlpatterns = [
    path('production/list/', ProductionListView.as_view(), name='production-list'),
    path('production_short/list/', ProductionShortListView.as_view(), name='production_short-list'),
    ]
