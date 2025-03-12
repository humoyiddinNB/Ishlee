from django.shortcuts import render
from django.contrib.auth.models import User

def homepageView(request):
    return render(request, 'homepage.html', {'user' : request.user})




