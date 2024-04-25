from django.urls import path
from django.contrib.auth.views import LoginView
from .views import LoginUser    


app_name = 'authentication'


urlpatterns = [
    path('', LoginUser.as_view(), name='login')
]
