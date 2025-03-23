from django.contrib import admin
from .models import Denuncia, TipoProblema, Anexo

@admin.register(TipoProblema)
class TipoProblemaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo_problema', 'data_hora')
    list_filter = ('tipo_problema', 'data_hora')
    search_fields = ('descricao',)

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('arquivo', 'denuncia')
    list_filter = ('denuncia',)