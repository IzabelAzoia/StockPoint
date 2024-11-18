# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockpoint.settings')
django.setup()

import string
import timeit
from random import choice, random, randint
from stockpoint.produtos.models import Produto


class Utils:
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    "Ração Premium para Cães Adultos 15kg",
    "Ração para Gatos Filhotes 1kg",
    "Cama para Cachorro Pequeno",
    "Arranhador para Gatos 50cm",
    "Shampoo Hipoalergênico para Cães e Gatos 500ml",
    "Coleira Antipulgas e Carrapatos para Cães",
    "Brinquedo Mordedor para Cães (Corda)",
    "Areia Sanitária para Gatos 4kg",
    "Vitaminas para Cães e Gatos 100ml",
    "Escova Dental para Cães e Gatos",
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()

print('tempo:', toc - tic)
