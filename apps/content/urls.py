from django.urls import path

from apps.content.views import VideoListView, LogoCompanyListView


urlpatterns = [
    path('video/list/', VideoListView.as_view(), name='video-list'),
    path('logo_company/list/', LogoCompanyListView.as_view(), name='logo_company-list'),
    ]
