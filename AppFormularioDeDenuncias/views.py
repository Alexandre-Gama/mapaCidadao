from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Denuncia, TipoProblema, Anexo
from .forms import DenunciaForm, AnexoFormSet
from django.utils import timezone

def pagina_inicial(request):
    # Buscar algumas estatísticas básicas para exibir na página inicial
    total_denuncias = Denuncia.objects.count()
    tipos_problema = TipoProblema.objects.all()
    return render(request, 'app/pagina_inicial.html', {
        'total_denuncias': total_denuncias,
        'tipos_problema': tipos_problema
    })

def formulario_denuncia(request):
    tipos_problema = TipoProblema.objects.all()
    
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        formset = AnexoFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            denuncia = form.save(commit=False)
            denuncia.data_hora = timezone.now()
            denuncia.save()
            
            # Salvar anexos
            anexos = formset.save(commit=False)
            for anexo in anexos:
                anexo.denuncia = denuncia
                anexo.save()
            
            messages.success(request, 'Denúncia registrada com sucesso!')
            return redirect('mapa_denuncias')
    else:
        form = DenunciaForm()
        formset = AnexoFormSet()
    
    return render(request, 'app/app_formulariodedenuncias.html', {
        'form': form,
        'formset': formset,
        'tipos_problema': tipos_problema,
    })