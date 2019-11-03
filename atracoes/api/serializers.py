from atracoes.models import *
from rest_framework.serializers import ModelSerializer

class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['nome', 'descricao','horario_func','idade_minima','foto']
