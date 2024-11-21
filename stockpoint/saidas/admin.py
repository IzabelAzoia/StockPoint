from django.contrib import admin
from .models import Saida

class SaidaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'fornecedor', 'quantity', 'created_at')  
    search_fields = ('produto__nome', 'fornecedor__nome')

admin.site.register(Saida, SaidaAdmin)