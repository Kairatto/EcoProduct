from django.urls import path

from apps.brand_info.views import BrandHistoryListView, BrandInfoListView


urlpatterns = [
    path('brand_history/list/', BrandHistoryListView.as_view(), name='brand_history-list'),
    path('brand_info/list/', BrandInfoListView.as_view(), name='brand_info-list'),
    ]
