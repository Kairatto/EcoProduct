from django.urls import path

from apps.brand.views import BrandListView, BrandDetailView


urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand-list'),
    path('detail/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),

]
