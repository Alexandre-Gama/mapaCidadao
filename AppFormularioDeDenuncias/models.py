from django.db import models

# Modelo para o formulário de denúncias
class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    tipo_problema = models.ForeignKey('TipoProblema', on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.descricao

# Modelo para o tipo de problema (chave estrangeira)
class TipoProblema(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    
# Modelo para os anexos
class Anexo(models.Model):
    id = models.AutoField(primary_key=True)
    denuncia = models.ForeignKey('Denuncia', on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='anexos/')
    def __str__(self):
        return self.arquivo.name