from rest_framework import serializers
from django.db.models import Q
from casting.models import Pessoa

# Admin serializers


class PessoaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class AtorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FiguracaoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class ModeloMasculinoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class ModeloFemininoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class CriancaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

# Non-admin serializers


class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_artistico', 'ano', 'DRT', 'altura',
                  'manequim', 'sapato', 'foto3x4', 'foto_corpo_inteiro', 'foto_com_sorriso']


class FiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_artistico', 'ano', 'altura',
                  'manequim', 'sapato', 'foto3x4', 'foto_corpo_inteiro', 'foto_com_sorriso']


class ModeloMasculinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_artistico', 'ano', 'altura',
                  'manequim', 'sapato', 'foto3x4', 'foto_corpo_inteiro', 'foto_com_sorriso', 'camisa']


class ModeloFemininoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_artistico', 'ano', 'altura',
                  'manequim', 'sapato', 'foto3x4', 'foto_corpo_inteiro', 'foto_com_sorriso',
                  'busto', 'cintura', 'quadril']


class CriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_artistico', 'ano', 'foto3x4', 'foto_corpo_inteiro', 'foto_com_sorriso',
                  'data_nascimento']
