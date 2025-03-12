from django.urls import path
from .views import homepageView


app_name = 'homepage'
urlpatterns = [
    path('', homepageView, name='homepage'),
]