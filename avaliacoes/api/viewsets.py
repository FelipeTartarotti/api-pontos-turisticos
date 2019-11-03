from django.shortcuts import render
from avaliacoes.models import *
from rest_framework import viewsets
from avaliacoes.api.serializers import *

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
