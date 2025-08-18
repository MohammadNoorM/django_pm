from django.contrib.auth.forms import AuthenticationForm
from django import forms

attrs = {'class': 'form-control'}


class LoginForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )
