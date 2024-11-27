from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categoria', 'marca', 'cost_price', 'selling_price', 'serie_number', 'quantity')
    
    search_fields = ('title', 'serie_number')
    
    list_filter = ('categoria', 'marca')
    
    ordering = ('title',)