from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import VacancyForm, VacancyUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, View, ListView, DeleteView
from .models import Vacancy


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'create_vacancy.html'
    def get_success_url(self):
        return reverse('vacancy:vacancy_details', kwargs={'pk' : self.object.pk})
    login_url = 'users:login'
    redirect_field_name = 'next'


class AllVacanciesView(View):
    def get(self, request):
        all_vacancies = Vacancy.objects.all()

        query = request.GET.get('q', '')
        if query:
            all_vacancies = all_vacancies.filter(title__icontains=query)

        all = all_vacancies.count()

        paginator = Paginator(all_vacancies, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        vacancies = page_obj.object_list



        context = {
            'page_obj': page_obj,
            'vacancies' : vacancies,
            'all' : all,
            'query' : query
        }
        return render(request, 'all_vacancies.html', context)

class VacancyDetailView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        context = {
            'vacancy' : vacancy
        }
        return render(request, 'vacancy_details.html' , context)



class VacancyUpdateView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        form = VacancyUpdateForm(instance=vacancy)
        context = {
            'vacancy' : vacancy,
            'form' : form
        }
        return render(request, 'vacancy_update.html', context)

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id=pk)
        form = VacancyUpdateForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy:vacancy_details', pk=vacancy.id)
        context = {
            'vacancy': vacancy,
            'form': form
        }
        return render(request, 'vacancy_update.html', context)


class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancy_delete.html'
    context_object_name = 'vacancy'
    success_url = reverse_lazy('vacancy:all_vacancies')

