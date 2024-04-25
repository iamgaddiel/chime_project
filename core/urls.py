from django.urls import path, include

from .views import Dashboard



app_name = 'core'


urlpatterns = [
    path('', include('authentication.urls')),
    path('inventory/', include('inventory.urls')),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
] 
