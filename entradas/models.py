from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor


class Entrada(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, related_name='entradas')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, related_name='entradas')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.produto)