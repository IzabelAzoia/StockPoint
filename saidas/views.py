from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import models, forms


class SaidaListView(ListView):
    model = models.Saida
    template_name = 'saida_list.html'
    context_object_name = 'saidas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(product__title__icontains=produto)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_metrics'] = metrics.get_produto_metrics()
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context


class SaidaCreateView(CreateView):
    model = models.Saida
    template_name = 'saida_create.html'
    form_class = forms.SaidaForm
    success_url = reverse_lazy('saida_list')


class SaidaDetailView(DetailView):
    model = models.Saida
    template_name = 'saida_detail.html'