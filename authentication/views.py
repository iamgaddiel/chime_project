from django.shortcuts import render
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    template_name = 'authentication/login.html'