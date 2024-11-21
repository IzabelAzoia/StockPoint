from django.urls import path
from . import views


urlpatterns = [
    path('categorias/list/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/create/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/detail/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
] 