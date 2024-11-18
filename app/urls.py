from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('', include('fornecedores.urls')),
    path('', include('marcas.urls')),
    path('', include('categorias.urls')),
    path('', include('produtos.urls')),
    path('', include('entradas.urls')),
    path('', include('saidas.urls')),
]