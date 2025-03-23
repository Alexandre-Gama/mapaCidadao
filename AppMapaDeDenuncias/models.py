from django.db import models
from django.contrib.auth.models import User
from AppFormularioDeDenuncias.models import Denuncia, TipoProblema, Anexo

# Modelo para configurações de visualização do mapa
class ConfiguracaoMapa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    zoom_padrao = models.IntegerField(default=13)
    latitude_central = models.FloatField(default=-23.550520)
    longitude_central = models.FloatField(default=-46.633309)
    mostrar_legendas = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Configuração de {self.usuario.username}"

# Modelo para filtros salvos
class FiltroSalvo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipos_problemas = models.ManyToManyField(TipoProblema)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nome

# Modelo para estatísticas de visualização
class EstatisticaVisualizacao(models.Model):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)
    visualizacoes = models.IntegerField(default=0)
    ultima_visualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Estatísticas de {self.denuncia.descricao}"