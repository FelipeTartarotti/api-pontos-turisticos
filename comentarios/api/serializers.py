from comentarios.models import *
from rest_framework.serializers import ModelSerializer

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['usuario', 'comentario','data','aprovado']


