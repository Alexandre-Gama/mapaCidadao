from django import forms
from django.forms import inlineformset_factory
from .models import Denuncia, Anexo, TipoProblema

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['descricao', 'tipo_problema', 'latitude', 'longitude']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_problema': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

# Formset simplificado para anexos (apenas um campo, sem opção de excluir)
AnexoFormSet = inlineformset_factory(
    Denuncia, 
    Anexo,
    fields=('arquivo',),
    extra=1,
    can_delete=False,
    widgets={'arquivo': forms.FileInput(attrs={'class': 'form-control'})}
)