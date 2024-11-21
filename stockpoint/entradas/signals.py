from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entrada


@receiver(post_save, sender=Entrada)
def update_produto_quantity(sender, instance, **kwargs):
    if instance.quantity > 0:
        produto = instance.produto
        produto.quantity += instance.quantity
        produto.save()