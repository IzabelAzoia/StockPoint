from django.contrib import admin
from .models import Saida

class SaidaAdmin(admin.ModelAdmin):
    # Certifique-se de que os campos listados realmente existem no modelo Saida
    list_display = ('produto', 'fornecedor', 'quantity', 'created_at')  
    search_fields = ('produto__nome', 'fornecedor__nome')  # Adiciona pesquisa pelos campos relacionados

admin.site.register(Saida, SaidaAdmin)