from django.urls import path

from apps.production.views import (ProductionListView, ProductionShortListView, ProductionProcessListView,
                                   ProductionPathListView)


urlpatterns = [
    path('production/list/', ProductionListView.as_view(), name='production-list'),
    path('production_short/list/', ProductionShortListView.as_view(), name='production_short-list'),
    path('production_process/list/', ProductionProcessListView.as_view(), name='production_process-list'),
    path('production_path/list/', ProductionPathListView.as_view(), name='production_path-list'),

]
