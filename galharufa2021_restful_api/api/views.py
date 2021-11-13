from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.db.models import Q
from .serializers import PessoaAdminSerializer, AtorAdminSerializer, FiguracaoAdminSerializer, ModeloMasculinoAdminSerializer, ModeloFemininoAdminSerializer, CriancaAdminSerializer
from .serializers import AtorSerializer, FiguracaoSerializer, ModeloMasculinoSerializer, ModeloFemininoSerializer, CriancaSerializer
from casting.models import Pessoa


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/pessoas-admin/'},
        {'GET': '/api/atores-admin/'},
        {'GET': '/api/figuracoes-admin/'},
        {'GET': '/api/modelos-admin/'},
        {'GET': '/api/criancas-admin/'},

        {'GET': '/api/pessoa-admin/slug'},
        {'GET': '/api/ator-admin/slug'},
        {'GET': '/api/figuracao-admin/slug'},
        {'GET': '/api/modelo-admin/slug'},
        {'GET': '/api/crianca-admin/slug'},


        {'GET': '/api/atores/'},
        {'GET': '/api/figuracoes/'},
        {'GET': '/api/modelos/'},
        {'GET': '/api/criancas/'},

        {'GET': '/api/ator/slug'},
        {'GET': '/api/figuracao/slug'},
        {'GET': '/api/modelo/slug'},
        {'GET': '/api/crianca/slug'},

        # {'POST':'/api/pessoa/cadastrar'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]

    return Response(routes)

# Admin views


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getPessoasAdmin(request):
    pessoas = Pessoa.objects.all()
    serializer = PessoaAdminSerializer(pessoas, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getAtoresAdmin(request):
    atores = Pessoa.objects.filter(tipo='ator').all()
    serializer = AtorAdminSerializer(atores, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getFiguracoesAdmin(request):
    figuracoes = Pessoa.objects.filter(tipo='figuracao').all()
    serializer = FiguracaoAdminSerializer(figuracoes, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getModelosMasculinosAdmin(request):
    modelos = Pessoa.objects.filter(
        Q(tipo='modelo'), Q(sexo='masculino')).all()
    serializer = ModeloMasculinoAdminSerializer(modelos, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getModelosFemininosAdmin(request):
    modelos = Pessoa.objects.filter(
        Q(tipo='modelo'), Q(sexo='feminino')).all()
    serializer = ModeloFemininoAdminSerializer(modelos, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getCriancasAdmin(request):
    criancas = Pessoa.objects.filter(tipo='crianca').all()
    serializer = CriancaAdminSerializer(criancas, many=True)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getPessoaAdmin(request, slug):
    pessoa = Pessoa.objects.get(slug=slug)
    serializer = PessoaAdminSerializer(pessoa, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getAtorAdmin(request, slug):
    ator = Pessoa.objects.get(Q(tipo='ator'), Q(slug=slug))
    serializer = AtorAdminSerializer(ator, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getFiguracaoAdmin(request, slug):
    figuracao = Pessoa.objects.get(Q(tipo='figuracao'), Q(slug=slug))
    serializer = FiguracaoAdminSerializer(figuracao, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getModeloMasculinoAdmin(request, slug):
    modelo = Pessoa.objects.get(
        Q(tipo='modelo'), Q(sexo='masculino'), Q(slug=slug))
    serializer = ModeloMasculinoAdminSerializer(modelo, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getModeloFemininoAdmin(request, slug):
    modelo = Pessoa.objects.get(
        Q(tipo='modelo'), Q(sexo='feminino'), Q(slug=slug))
    serializer = ModeloFemininoAdminSerializer(modelo, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@api_view(['GET'])
def getCriancaAdmin(request, slug):
    crianca = Pessoa.objects.get(Q(tipo='crianca'), Q(slug=slug))
    serializer = CriancaAdminSerializer(crianca, many=False)
    return Response(serializer.data)


# @permission_classes([IsAdminUser])
# @api_view(['POST'])
# def postPessoa(request):
#     data = request.data
#     current_user = request.user
#     pessoa = Pessoa.objects.create(pessoa=data)
#     serializer = PessoaSerializer(pessoa, many = False)
#     return Response(serializer.data)

# Non-admin views


@api_view(['GET'])
def getAtores(request):
    atores = Pessoa.objects.filter(tipo='ator').all()
    serializer = AtorSerializer(atores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFiguracoes(request):
    figuracoes = Pessoa.objects.filter(tipo='figuracao').all()
    serializer = FiguracaoSerializer(figuracoes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getModelosMasculinos(request):
    modelos = Pessoa.objects.filter(
        Q(tipo='modelo'), Q(sexo='masculino')).all()
    serializer = ModeloMasculinoSerializer(modelos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getModelosFemininos(request):
    modelos = Pessoa.objects.filter(
        Q(tipo='modelo'), Q(sexo='feminino')).all()
    serializer = ModeloFemininoSerializer(modelos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCriancas(request):
    criancas = Pessoa.objects.filter(tipo='crianca').all()
    serializer = CriancaSerializer(criancas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAtor(request, slug):
    ator = Pessoa.objects.get(Q(tipo='ator'), Q(slug=slug))
    serializer = AtorSerializer(ator, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getFiguracao(request, slug):
    figuracao = Pessoa.objects.get(Q(tipo='figuracao'), Q(slug=slug))
    serializer = FiguracaoSerializer(figuracao, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getModeloMasculino(request, slug):
    modelo = Pessoa.objects.get(
        Q(tipo='modelo'), Q(sexo='masculino'), Q(slug=slug))
    serializer = ModeloMasculinoSerializer(modelo, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getModeloFeminino(request, slug):
    modelo = Pessoa.objects.get(
        Q(tipo='modelo'), Q(sexo='feminino'), Q(slug=slug))
    serializer = ModeloFemininoSerializer(modelo, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getCrianca(request, slug):
    crianca = Pessoa.objects.get(Q(tipo='crianca'), Q(slug=slug))
    serializer = CriancaSerializer(crianca, many=False)
    return Response(serializer.data)
