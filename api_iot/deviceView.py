from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api_iot.deviceModel import DeviceModel
from api_iot.deviceSerializer import DeviceSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

def device_list(request):
    device = DeviceModel.objects.last()
    return render(request, 'template.html', {'device': device})
