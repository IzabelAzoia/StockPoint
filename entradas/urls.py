from django.urls import path
from . import views


urlpatterns = [
    path('entradas/list/', views.EntradaListView.as_view(), name='entrada_list'),
    path('entradas/create/', views.EntradaCreateView.as_view(), name='entrada_create'),
    path('entradas/<int:pk>/detail/', views.EntradaDetailView.as_view(), name='entrada_detail'),
]