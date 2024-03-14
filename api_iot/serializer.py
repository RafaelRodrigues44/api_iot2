from rest_framework import serializers
from api_iot.deviceModels import DeviceModel

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ['id', 'Sensor', 'Botao', 'LigaRobo', 'ResetContador', 'ValorContagem']
