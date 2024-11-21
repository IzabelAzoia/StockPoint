from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import models, forms
from fornecedores.models import Fornecedor


class SaidaListView(ListView):
    model = models.Saida
    template_name = 'saida_list.html'
    context_object_name = 'saidas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(produto__title__icontains=produto)

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

    def form_valid(self, form):
        
        fornecedor = Fornecedor.objects.first()
        if fornecedor:
            form.instance.fornecedor = fornecedor 
        
        return super().form_valid(form)


class SaidaDetailView(DetailView):
    model = models.Saida
    template_name = 'saida_detail.html'