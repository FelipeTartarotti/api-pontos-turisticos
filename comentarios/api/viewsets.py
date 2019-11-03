from django.shortcuts import render
from comentarios.models import *
from rest_framework import viewsets
from comentarios.api.serializers import *

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
