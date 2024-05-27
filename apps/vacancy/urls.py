from django.urls import path

from apps.vacancy.views import VacancyListView, DefaultVacancyListView, VacancyDetailView


urlpatterns = [
    path('list/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancy/detail/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('default/list/', DefaultVacancyListView.as_view(), name='default_vacancy-list'),
    ]
