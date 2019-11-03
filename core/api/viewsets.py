from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import *

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']

    def get_queryset(self): #Retorno de lista ou queryset customizado
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs ):  #Sobreescrever método list que é disparado no GET e retorna um lista
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs ): #Sobreescrever método POST
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):  # Sobreescrever método DELETE
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # Sobreescrever método GET (usar para objetos e validações)
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs): # Sobreescrever método PUT
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs): # Sobreescrever método PATCH
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post','get'], detail=True)          # Criar uma novo metodo para receber requisições
    def denunciar(self, request, pk=None):                # pontosturisticos/1/denunciar/
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=id)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return Response("Ok")

