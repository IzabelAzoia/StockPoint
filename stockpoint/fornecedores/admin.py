from django.contrib import admin
from . import models


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


admin.site.register(models.Fornecedor, FornecedorAdmin)