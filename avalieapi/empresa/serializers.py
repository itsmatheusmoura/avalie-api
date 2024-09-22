from django.contrib.auth.models import Group, User
from rest_framework import serializers
from avalieapi.empresa.models import Empresa, Pergunta, Avaliacao


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'email', 'telefone', 'endereco', 'cidade', 'estado', 'cep']

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = ['id', 'descricao', 'empresa']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['pergunta', 'resposta', 'comentario', 'data', 'empresa']

