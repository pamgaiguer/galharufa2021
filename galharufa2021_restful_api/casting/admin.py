from django.contrib import admin
from .models import Endereco, DadosBancarios, Pessoa

# Register your models here.


class PessoaAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)


admin.site.register(Endereco)
admin.site.register(DadosBancarios)
admin.site.register(Pessoa, PessoaAdmin)
