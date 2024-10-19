from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


# ViewSet para o modelo de usuários
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar usuários.
    O DRF fornece o comportamento CRUD completo automaticamente usando o ModelViewSet
    """

    # Define o queryset, que são os dados recuperados do banco de dados
    queryset = User.objects.all().order_by("-date_joined")
    # Define o serializador que será usado para converter os objetos User em JSON e vice-versa
    serializer_class = UserSerializer
    # Permissão: apenas usuários autenticados podem acessar este endpoint
    permission_classes = [permissions.IsAuthenticated]


# ViewSet para o modelo de grupos
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar grupos.
    O DRF gerencia automaticamente as operações CRUD pelo ModelViewSet
    """

    # Recupera todos os grupos e os ordena por nome
    queryset = Group.objects.all().order_by("name")
    # Usa o GroupSerializer para serializar e desserializar os dados
    serializer_class = GroupSerializer
    # Apenas usuários autenticados podem acessar esse endpoint
    permission_classes = [permissions.IsAuthenticated]
