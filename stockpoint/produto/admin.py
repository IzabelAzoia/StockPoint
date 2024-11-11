from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class Produtoadmin(admin.ModelAdmin):
    list_display=(
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields=('produto',)
    list_filter=('importado',)