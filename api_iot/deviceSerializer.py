from rest_framework import serializers
from api_iot.deviceModel import DeviceModel

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ['id', 'Sensor', 'Botao', 'LigaRobo', 'ResetContador', 'ValorContagem']
