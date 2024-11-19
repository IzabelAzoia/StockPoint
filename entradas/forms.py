from django import forms
from . import models


class EntradaForm(forms.ModelForm):

    class Meta:
        model = models.Entrada
        fields = ['fornecedor', 'produto', 'quantity', 'description']
        widgets = {
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'fornecedor': 'Fornecedor',
            'produto': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }