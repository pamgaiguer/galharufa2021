from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

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
