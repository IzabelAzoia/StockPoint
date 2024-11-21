from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('fornecedores/', include('fornecedores.urls')),
    path('marcas/', include('marcas.urls')),
    path('categorias/', include('categorias.urls')),
    path('produtos/', include('produtos.urls')),
    path('entradas/', include('entradas.urls')),
    path('saidas/', include('saidas.urls')),
]