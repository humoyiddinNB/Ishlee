from django.urls import path
from .views import VacancyCreateView, AllVacanciesView, VacancyDetailView, VacancyUpdateView, VacancyDeleteView


app_name = 'vacancy'
urlpatterns = [
    path('create/', VacancyCreateView.as_view(), name='create_vacancy'),
    path('all/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('details/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_details'),
    path('update/<int:pk>/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('delete/<int:pk>/', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('search/', AllVacanciesView.as_view(), name='vacancy_search'),
]