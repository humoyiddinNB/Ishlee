from .models import Vacancy
from django import forms

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'requirements', 'salary', 'location', 'contact']

class VacancyUpdateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'company', 'requirements', 'salary', 'location', 'contact']