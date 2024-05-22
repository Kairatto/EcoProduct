from django.urls import path

from apps.news.views import NewsListView


urlpatterns = [
    path('list/', NewsListView.as_view(), name='news-list'),
    ]
