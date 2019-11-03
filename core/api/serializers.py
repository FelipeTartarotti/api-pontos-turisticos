from rest_framework.fields import SerializerMethodField

from core.models import *
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecosSerializer(read_only=True)
    descricao_completa = SerializerMethodField() #Add new method in the serializers and return the result in the serializer
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','aprovado','foto',
                  'atracoes', 'comentarios','avaliacoes','endereco',
                  'descricao_completa','descricao_completa2', 'doc_identificacao')#descricao_completa2 is a property you can find in core.models
        read_only_fields = ('comentarios','avaliacoes') #Read only means that it`s not needed to pass this information in the post, because you can only read.

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self,validated_data): #Create custom method to add atracoes and endereco (M2M en FK) to PontoTuristico posting with the same JSON
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)


        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)


