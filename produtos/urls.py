# urls.py
from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),  # Usando ProdutoListView
    path('criar/', ProdutoCreateView.as_view(), name='produto_create'),  # Usando ProdutoCreateView
    path('<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),  # Usando ProdutoDetailView
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),  # Usando ProdutoUpdateView
    path('<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto_delete'),  # Usando ProdutoDeleteView
]
