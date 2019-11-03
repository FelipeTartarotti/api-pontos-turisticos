from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from atracoes.models import *
from rest_framework import viewsets
from atracoes.api.serializers import *
# Create your views here.

class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'nome','descricao'}
