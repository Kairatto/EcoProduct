from django.urls import path

from apps.product.views import BrandView

urlpatterns = [
    path('list/', BrandView.as_view(), name='brand-list'),

]
