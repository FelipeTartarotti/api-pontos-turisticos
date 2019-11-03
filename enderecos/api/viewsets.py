from django.shortcuts import render
from enderecos.models import *
from rest_framework import viewsets
from enderecos.api.serializers import *
# Create your views here.

class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
