from django.urls import path, include
from .modelViews import DeviceView, DevicePostView
from rest_framework. routers import DefaultRouter

router = DefaultRouter()
router.register("", DevicePostView)

urlpatterns = [
    path('dispositivos/', DeviceView.as_view(), name='lista_dispositivos'),
    path('dispositivos/post/', include(router.urls), name='device_create' ),
]
