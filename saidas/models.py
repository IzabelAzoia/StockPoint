from django.db import models
from produtos.models import Produto


class Saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='saidas')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.produto)