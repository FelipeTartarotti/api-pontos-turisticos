from enderecos.models import *
from rest_framework.serializers import ModelSerializer

class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['linha1', 'linha2','cidade','estado','pais','longitude','latitude']
