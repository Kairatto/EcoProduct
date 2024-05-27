from django.urls import path

from apps.production.views import ProductionListView, ProductionShortListView, ProductionDetailView


urlpatterns = [
    path('production/list/', ProductionListView.as_view(), name='production-list'),
    path('production/detail/<int:pk>/', ProductionDetailView.as_view(), name='product-detail'),
    path('production_short/list/', ProductionShortListView.as_view(), name='production_short-list'),

]
