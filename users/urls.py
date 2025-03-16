from django.urls import path
from .views import RegisterView, ProfileView, login_user, log_out, ProfileUpdateView

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='user_profile'),
    path('login/', login_user, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update')
]
