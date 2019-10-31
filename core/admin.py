from django.contrib import admin
from .models import *


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

    search_fields = ('nome',)
    list_filter = ("nome",)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'complemento',
                    'bairro', 'cidade', 'uf', 'cep')

    search_fields = ('bairro', 'cidade', 'logradouro', 'complemento')
    list_filter = ('bairro', 'cidade', 'uf')


class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cor_toalha', 'valor_aluguel')
    list_filter = ('cor_toalha', 'valor_aluguel')
    search_fields = ('nome',)
    filter_horizontal = ('item',)


class AluguelAdmin(admin.ModelAdmin):
    list_display = ("data_festa", "hora_inicio", "hora_termino", "valor_cobrado")
    date_hierarchy = "data_festa"
    list_filter = ("data_festa", "valor_cobrado")


admin.site.site_header = "Painel de controle"
admin.site.site_title = "Administração de festa"
admin.site.index_title = "Recurso"

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ItemTema, ItemAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Aluguel, AluguelAdmin)
