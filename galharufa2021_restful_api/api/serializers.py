from rest_framework import serializers
from casting.models import Pessoa

class PessoaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'