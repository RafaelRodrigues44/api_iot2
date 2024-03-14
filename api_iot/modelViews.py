from django.views.generic import ListView, View
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from api_iot.deviceModels import DeviceModel
from api_iot.serializer import DispositivoSerializer
from rest_framework.response import Response

class DeviceView(ListView):
    model = DeviceModel
    template_name = 'template.html'
    context_object_name = 'dispositivos'

    def get_queryset(self):
        return DeviceModel.objects.all()

class DevicePostView(viewsets.ModelViewSet):
        
        serializer_class = DispositivoSerializer
        queryset = DeviceModel.objects.all()



        """
        #def get(self, request, *args, **kwargs):
        dispositivos = DeviceModel.objects.all()
        return render(request, 'template.html', {'dispositivos': dispositivos})

    #def post(self, request, *args, **kwargs):
        new_device = DeviceModel.objects.create(
            sensor=request.POST.get('sensor'),
            button=request.POST.get('button'),
            robot_on=request.POST.get('robot_on'),
            reset_counter=request.POST.get('reset_counter'),
            count_value=request.POST.get('count_value')
        )
        return JsonResponse({'success': True})
        """
