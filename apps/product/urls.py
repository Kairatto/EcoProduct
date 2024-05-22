from django.urls import path

from apps.product.views import ProductListView, VolumeListView, VolumeDetailView


urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('volume/list/', VolumeListView.as_view(), name='volume-list'),
    path('volume/detail/<int:pk>/', VolumeDetailView.as_view(), name='volume-detail'),

]
