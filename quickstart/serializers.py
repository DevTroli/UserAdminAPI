from django.contrib.auth.models import Group, User
from rest_framework import serializers


# Serializer para o modelo de usuário
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Usamos HyperlinkedModelSerializer para incluir URLs relacionadas aos usuários.
    """

    class Meta:
        # Modelo referenciado
        model = User
        # Campos que serão incluídos na resposta JSON
        fields = ["url", "username", "email", "groups"]


# Serializer para o modelo de grupo de usuários
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para o modelo Group.
    Apenas o campo 'name' será incluído.
    """

    class Meta:
        # Modelo referenciado
        model = Group
        # Campos que serão incluídos na resposta JSON
        fields = ["name"]
