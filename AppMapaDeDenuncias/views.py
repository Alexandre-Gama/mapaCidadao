from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from AppFormularioDeDenuncias.models import Denuncia, TipoProblema
from .models import EstatisticaVisualizacao
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json

def mapa_denuncias(request):
    tipos_problema = TipoProblema.objects.all()
    return render(request, 'app/app_mapadedenuncias.html', {
        'tipos_problema': tipos_problema
    })

def api_denuncias(request):
    # Parâmetros de filtro
    tipo_id = request.GET.get('tipo')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    
    denuncias = Denuncia.objects.all()
    
    # Aplicar filtros se fornecidos
    if tipo_id:
        denuncias = denuncias.filter(tipo_problema_id=tipo_id)
    if data_inicio:
        denuncias = denuncias.filter(data_hora__gte=data_inicio)
    if data_fim:
        denuncias = denuncias.filter(data_hora__lte=data_fim)
    
    # Construir resposta JSON
    denuncias_json = []
    for denuncia in denuncias:
        # Registrar visualização
        estatistica, created = EstatisticaVisualizacao.objects.get_or_create(
            denuncia=denuncia
        )
        estatistica.visualizacoes += 1
        estatistica.save()
        
        denuncias_json.append({
            'id': denuncia.id,
            'descricao': denuncia.descricao,
            'data_hora': denuncia.data_hora.strftime('%d/%m/%Y %H:%M'),
            'tipo_problema': denuncia.tipo_problema.descricao,
            'latitude': denuncia.latitude,
            'longitude': denuncia.longitude,
            'tipo_problema_id': denuncia.tipo_problema.id,
            'visualizacoes': estatistica.visualizacoes,
        })
    
    return JsonResponse({'denuncias': denuncias_json})

def detalhe_denuncia(request, denuncia_id):
    denuncia = get_object_or_404(Denuncia, id=denuncia_id)
    anexos = denuncia.anexo_set.all()
    
    # Atualizar estatísticas
    estatistica, created = EstatisticaVisualizacao.objects.get_or_create(
        denuncia=denuncia
    )
    estatistica.visualizacoes += 1
    estatistica.save()
    
    return render(request, 'app/detalhe_denuncia.html', {
        'denuncia': denuncia,
        'anexos': anexos,
        'estatistica': estatistica,
    })