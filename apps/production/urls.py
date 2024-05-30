from django.urls import path

from apps.production.views import ProductionShortListView


urlpatterns = [
    path('production_short/list/', ProductionShortListView.as_view(), name='production_short-list'),

]
