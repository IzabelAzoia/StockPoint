from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProdutoListView.as_view(), name='produto_list'),
    path('create/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/detail/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('<int:pk>/update/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]