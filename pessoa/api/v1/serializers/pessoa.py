from django.db import transaction
from rest_framework import serializers

from pessoa.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    # @transaction.atomic
    # def create(self, validated_data):
    #     return super(PessoaSerializer, self).create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     return super(PessoaSerializer, self).update(instance, validated_data)
    def validar_usuario(self):
        pass

# class Pessoa2Serializer(serializers.Serializer):
#     nome = serializers.CharField(required=False)