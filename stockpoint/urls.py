from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('stockpoint.core.urls')),
    path('produto/', include('stockpoint.produto.urls')),
    path('estoque/', include('stockpoint.estoque.urls')),
    path('admin/', admin.site.urls),
]
