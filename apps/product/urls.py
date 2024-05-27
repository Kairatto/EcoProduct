from django.urls import path

from apps.product.views import ProductListView, CategoryListView, CategoryDetailView, BrandView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('list_2/', BrandView.as_view(), name='brand-list'),
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]
