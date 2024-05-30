from django.urls import path

from apps.language.views import LanguageListView

urlpatterns = [
    path('list/', LanguageListView.as_view(), name='language-list'),

]
