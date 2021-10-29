from django.contrib import admin
from .models import Endereco, DadosBancarios, Pessoa

# Register your models here.

admin.site.register(Endereco)
admin.site.register(DadosBancarios)
admin.site.register(Pessoa)