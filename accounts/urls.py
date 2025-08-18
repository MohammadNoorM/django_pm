from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import LoginForm
from accounts.views import RegistrationView, edit_profile

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
]