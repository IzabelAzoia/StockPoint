from django.urls import path
from . import views


urlpatterns = [
    path('fornecedores/list/', views.FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/create/', views.FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<int:pk>/detail/', views.FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedores/<int:pk>/update/', views.FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<int:pk>/delete/', views.FornecedorDeleteView.as_view(), name='fornecedor_delete'),
]