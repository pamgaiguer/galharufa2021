from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.

class Endereco(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # pais
    # estado
    # cidade
    # bairro
    # rua
    # numero
    # casa/apto


class DadosBancarios(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # banco
    # agencia
    # conta


class Pessoa(models.Model):
    SEXO = (
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino')
    )
    TIPO = (
        ('ator', 'Ator'),
        ('figuracao', 'Figuração'),
        ('modelo', 'Modelo'),
        ('crianca', 'Criança')
    )
    VEICULO = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('trator', 'Trator'),
        ('jetski', 'JetSki')
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, editable=False)
    sexo = models.CharField(max_length=9, choices=SEXO)
    tipo = models.CharField(max_length=9, choices=TIPO)
    nome_completo = models.CharField(max_length=200)
    nome_artistico = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)])
    DRT = models.CharField(validators=[RegexValidator(regex='^.{7}$', message='Length has to be 7!', code='nomatch')])
    altura = models.FloatField()
    manequim = models.PositiveIntegerField()
    sapato = models.PositiveIntegerField()
    foto3x4 = models.ImageField()
    foto_corpo_inteiro = models.ImageField()
    foto_com_sorriso = models.ImageField()
    CNH = models.IntegerField(validators=[RegexValidator(regex='^.{10}$', message='Length has to be 11!', code='nomatch')])
    veiculo = models.CharField(max_length=6, choices=VEICULO)
    portfolio = models.URLField()
    peso = models.IntegerField()
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True)
    RG = models.IntegerField(validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10!', code='nomatch')])
    CPF = models.IntegerField(validators=[RegexValidator(regex='^.{11}$', message='Length has to be 11!', code='nomatch')]) 
    terno = models.PositiveIntegerField(null=True) # homens
    camisa = models.PositiveIntegerField(null=True) # homens
    busto = models.PositiveIntegerField(null=True) # mulheres
    cintura = models.PositiveIntegerField(null=True) # mulheres
    quadril = models.PositiveIntegerField(null=True) # mulheres
    data_nascimento = models.DateField()
    habilidades = models.TextField()
    dados_bancarios = models.OneToOneField(DadosBancarios, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
         self.slug = slugify(self.nome_artistico)
         super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_completo} ({self.tipo})"
