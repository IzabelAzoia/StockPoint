# urls.py
from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoDetailView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('criar/', ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
