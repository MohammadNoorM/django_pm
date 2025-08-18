from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import LoginForm


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
]