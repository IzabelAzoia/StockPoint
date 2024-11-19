from django.contrib import admin
from . import models


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'produto', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('fornecedor__name', 'produto__title',)


admin.site.register(models.Entrada, EntradaAdmin)