from django.contrib import admin
from . import models


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


admin.site.register(models.Marca, MarcaAdmin)