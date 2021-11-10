from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import PessoaAdminSerializer
from casting.models import Pessoa

# VISIBLE FIELDS

# Ator:
#
# nome_artistico
# ano
# DRT
# altura
# manequim
# sapato
# foto3x4
# foto_corpo_inteiro
# foto_com_sorriso

# Figuracao:
#
# nome_artistico
# ano
# altura
# manequim
# sapato
# foto3x4
# foto_corpo_inteiro
# foto_com_sorriso

# Modelo (masculino):
#
# nome_artistico
# ano
# altura
# manequim
# sapato
# foto3x4
# foto_corpo_inteiro
# foto_com_sorriso
# camisa

# Modelo (feminino):
#
# nome_artistico
# ano
# altura
# manequim
# sapato
# foto3x4
# foto_corpo_inteiro
# foto_com_sorriso
# busto
# cintura
# quadril

# Crianca:
#
# nome_artistico
# ano
# foto3x4
# foto_corpo_inteiro
# foto_com_sorriso
# data_nascimento

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/pessoas-admin/'},
        {'GET':'/api/pessoa-admin/slug'},
        #{'POST':'/api/pessoa/cadastrar'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]

    return Response(routes)

@api_view(['GET'])
def getPessoasAdmin(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaAdminSerializer(pessoas, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getPessoaAdmin(request, slug):
    pessoa = Pessoa.objects.get(slug=slug)
    serializer = PessoaAdminSerializer(pessoa, many = False)
    return Response(serializer.data)

# @api_view(['POST'])
# def postPessoa(request):
#     data = request.data
#     current_user = request.user
#     pessoa = Pessoa.objects.create(pessoa=data)
#     serializer = PessoaSerializer(pessoa, many = False)
#     return Response(serializer.data)
