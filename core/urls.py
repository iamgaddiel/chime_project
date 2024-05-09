from django.urls import path, include

from .views import Dashboard, RecordList, RecordDetail



app_name = 'core'


urlpatterns = [
    path('', include('authentication.urls')),
    path('records/', RecordList.as_view(), name='records'),
    path('records/detail/<str:record_type>/<uuid:ref_id>/<str:action>/', RecordDetail.as_view(), name='record_detail'),
    path('inventory/', include('inventory.urls')),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
] 
