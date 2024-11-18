from django.contrib import admin
from . import models


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'serie_number',)
    search_fields = ('title',)


admin.site.register(models.Produto, ProdutoAdmin)