from django.urls import path

from apps.news.views import NewsListView, NewsDetailView


urlpatterns = [
    path('list/', NewsListView.as_view(), name='news-list'),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

]
