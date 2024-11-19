from django import forms
from django.core.exceptions import ValidationError
from . import models


class SaidaForm(forms.ModelForm):
    class Meta:
        model = models.Saida
        fields = ['produto', 'quantity', 'description']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'produto': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        produto = self.cleaned_data.get('produto')

        if quantity > produto.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {produto.title} é de {produto.quantity} unidades.'
            )

        return quantity