from avaliacoes.models import *
from rest_framework.serializers import ModelSerializer

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'usuario','comentario','nota','data']

