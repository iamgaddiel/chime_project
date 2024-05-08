from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import LoginUser    


app_name = 'authentication'


urlpatterns = [
    # path('', LoginUser.as_view(), name='login')
    path('', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
