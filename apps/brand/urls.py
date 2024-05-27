from django.urls import path

from apps.brand.views import BrandListView, BrandDetailView, AnotherProductsListView


urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand-list'),
    path('another/', AnotherProductsListView.as_view(), name='another-list'),
    path('detail/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),

]
