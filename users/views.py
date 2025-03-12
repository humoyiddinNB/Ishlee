from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users:user_profile', pk=user.pk)
        return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_profile', pk=user.pk)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('homepage:homepage')



class ProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, 'user_profile.html', {'user':user})