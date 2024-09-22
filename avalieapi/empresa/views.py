from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from avalieapi.empresa.models import Empresa, Pergunta, Avaliacao
from avalieapi.empresa.serializers import UserSerializer, GroupSerializer, EmpresaSerializer, PerguntaSerializer, \
    AvaliacaoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

    def get_queryset(self):
        queryset = Pergunta.objects.all().order_by('id')
        return queryset

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
