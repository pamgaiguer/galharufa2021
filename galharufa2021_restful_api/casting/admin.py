from django.contrib import admin
from .models import Endereco, DadosBancarios, Pessoa

# Register your models here.


class EnderecoAdmin(admin.ModelAdmin):
    list_filter = ("cidade", "estado")
    list_display = ("logradouro", "numero", "bairro", "cidade", "estado")


class DadosBancariosAdmin(admin.ModelAdmin):
    list_filter = ("banco",)
    list_display = ("banco", "agencia", "conta")


class PessoaAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("tipo",)
    list_display = ("nome_completo", "nome_artistico", "sexo", "tipo",)


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(DadosBancarios, DadosBancariosAdmin)
admin.site.register(Pessoa, PessoaAdmin)
