from django.urls import path
from api_iot.deviceView import device_list, DeviceViewSet

app_name = 'api_iot'

urlpatterns = [
    path('dispositivos/', device_list, name='device_list'),
    path('dispositivos/create/', DeviceViewSet.as_view({'post': 'create'})),
    path('dispositivos/<int:pk>/', DeviceViewSet.as_view({'delete': 'destroy'}), name='device-delete'),
]
