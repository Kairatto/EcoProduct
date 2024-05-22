from django.urls import path

from apps.vacancy.views import VacancyListView, DefaultVacancyListView


urlpatterns = [
    path('list/', VacancyListView.as_view(), name='vacancy-list'),
    path('default/list/', DefaultVacancyListView.as_view(), name='default_vacancy-list'),
    ]
