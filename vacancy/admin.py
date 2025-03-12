from django.contrib import admin
from vacancy.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'requirements', 'salary']
    list_filter = ['salary', 'company']
    search_list = ['title', 'salary']
    oredering = ['-created_at']
