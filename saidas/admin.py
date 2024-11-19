from django.contrib import admin
from . import models


class SaidaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('produto__title',)


admin.site.register(models.Saida, SaidaAdmin)