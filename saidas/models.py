from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor



class Saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='saidas')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='fornecedores')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def fornecedor_nome(self):
        return self.fornecedor.nome
    fornecedor_nome.short_description = 'Fornecedor'