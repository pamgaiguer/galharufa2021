from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.


class Endereco(models.Model):
    ESTADO = (
        ('AC', 'Acre - AC'),
        ('AL', 'Alagoas - AL'),
        ('AP', 'Amapá - AP'),
        ('AM', 'Amazonas - AM'),
        ('BA', 'Bahia - BA'),
        ('CE', 'Ceará - CE'),
        ('DF', 'Distrito Federal - DF'),
        ('ES', 'Espírito Santo - ES'),
        ('GO', 'Goiás - GO'),
        ('MA', 'Maranhão - MA'),
        ('MT', 'Mato Grosso - MT'),
        ('MS', 'Mato Grosso do Sul - MS'),
        ('MG', 'Minas Gerais - MG'),
        ('PA', 'Pará - PA'),
        ('PB', 'Paraíba - PB'),
        ('PR', 'Paraná - PR'),
        ('PE', 'Pernambuco - PE'),
        ('PI', 'Piauí - PI'),
        ('RJ', 'Rio de Janeiro - RJ'),
        ('RN', 'Rio Grande do Norte - RN'),
        ('RS', 'Rio Grande do Sul - RS'),
        ('RO', 'Rondônia - RO'),
        ('RR', 'Roraima - RR'),
        ('SC', 'Santa Catarina - SC'),
        ('SP', 'São Paulo - SP'),
        ('SE', 'Sergipe - SE'),
        ('TO', 'Tocantins - TO'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    CEP = models.IntegerField(validators=[RegexValidator(
        regex='^.{8}$', message='O CEP necessita ter 8 caracteres!', code='nomatch')])
    estado = models.CharField(max_length=19, choices=ESTADO)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.cidade} ({self.estado[:2].upper()})"

    class Meta:
        verbose_name_plural = "Endereços"


class DadosBancarios(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banco = models.CharField(max_length=100)
    agencia = models.PositiveIntegerField()
    conta = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.banco}, {self.agencia} - {self.conta}"

    class Meta:
        verbose_name_plural = "Dados Bancários"


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

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, editable=False)
    sexo = models.CharField(max_length=9, choices=SEXO)
    tipo = models.CharField(max_length=9, choices=TIPO)
    nome_completo = models.CharField(max_length=200)
    nome_artistico = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(
        1900), MaxValueValidator(datetime.date.today().year)])
    DRT = models.CharField(blank=True, max_length=7, validators=[RegexValidator(
        regex='^.{7}$', message='O DRT necessita ter 7 caracteres!', code='nomatch')])
    altura = models.FloatField(blank=True)
    manequim = models.PositiveIntegerField(blank=True)
    sapato = models.PositiveIntegerField(blank=True)
    foto3x4 = models.ImageField(upload_to='static/images/3x4/')
    foto_corpo_inteiro = models.ImageField(
        upload_to='static/images/corpo_inteiro/')
    foto_com_sorriso = models.ImageField(
        upload_to='static/images/com_sorriso /')
    CNH = models.IntegerField(blank=True, validators=[RegexValidator(
        regex='^.{11}$', message='A CNH necessita ter 11 caracteres!', code='nomatch')])
    veiculo = models.CharField(blank=True, max_length=6, choices=VEICULO)
    portfolio = models.URLField(blank=True)
    peso = models.IntegerField(blank=True)
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, null=True)
    RG = models.IntegerField(validators=[RegexValidator(
        regex='^.{10}$', message='O RG necessita ter 10 caracteres!', code='nomatch')])
    CPF = models.IntegerField(validators=[RegexValidator(
        regex='^.{11}$', message='O CPF necessita ter 11 caracteres!', code='nomatch')])
    terno = models.PositiveIntegerField(null=True, blank=True)  # homens
    camisa = models.PositiveIntegerField(null=True, blank=True)  # homens
    busto = models.PositiveIntegerField(null=True, blank=True)  # mulheres
    cintura = models.PositiveIntegerField(null=True, blank=True)  # mulheres
    quadril = models.PositiveIntegerField(null=True, blank=True)  # mulheres
    data_nascimento = models.DateField()
    habilidades = models.TextField(blank=True)
    dados_bancarios = models.OneToOneField(
        DadosBancarios, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome_artistico)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_completo} ({self.tipo})"
