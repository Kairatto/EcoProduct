from django.urls import path

from apps.language.views import LanguageListView, LanguageDetailView

urlpatterns = [
    path('list/', LanguageListView.as_view(), name='language-list'),
    path('detail/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),

]
