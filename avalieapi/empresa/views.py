from django.contrib.auth.models import Group, User
from django.http import Http404
from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from avalieapi.empresa.models import Empresa, Pergunta, Avaliacao
from avalieapi.empresa.serializers import UserSerializer, GroupSerializer, EmpresaSerializer, PerguntaSerializer, \
    AvaliacaoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer

    def get_queryset(self):
        queryset = Pergunta.objects.all()
        empresa_id = self.request.query_params.get('empresa')

        if not empresa_id:
            raise ValidationError('O parâmetro "empresa" é obrigatório.')

        try:
            Empresa.objects.get(id=empresa_id)
        except Empresa.DoesNotExist:
            raise Http404('Empresa não encontrada.')

        queryset = queryset.filter(empresa_id=empresa_id)
        return queryset

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
