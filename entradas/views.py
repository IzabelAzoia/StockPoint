from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class EntradaListView(ListView):
    model = models.Entrada
    template_name = 'entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(product__title__icontains=produto)

        return queryset


class EntradaCreateView(CreateView):
    model = models.Entrada
    template_name = 'entrada_create.html'
    form_class = forms.EntradaForm
    success_url = reverse_lazy('entrada_list')


class EntradaDetailView(DetailView):
    model = models.Entrada
    template_name = 'entrada_detail.html'