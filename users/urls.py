from django.urls import path
from .views import RegisterView, ProfileView, login_user, log_out

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='user_profile'),
    path('login/', login_user, name='login'),
    path('logout/', log_out, name='logout')
]
