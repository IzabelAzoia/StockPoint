from django.urls import path
from . import views


urlpatterns = [
    path('saidas/list/', views.SaidaListView.as_view(), name='saida_list'),
    path('saidas/create/', views.SaidaCreateView.as_view(), name='saida_create'),
    path('saidas/<int:pk>/detail/', views.SaidaDetailView.as_view(), name='saida_detail'),
]