from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from marcas.models import Marca
from categorias.models import Categoria
from . import models, forms


class ProdutoListView(ListView):
    model = models.Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        categoria = self.request.GET.get('categoria')
        marca = self.request.GET.get('marca')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        if marca:
            queryset = queryset.filter(marca__id=marca)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_metrics'] = metrics.get_produto_metrics()
        context['sales_metrics'] = metrics.get_sales_metrics()
        context['categorias'] = Categoria.objects.all()
        context['marcas'] = Marca.objects.all()
        return context


class ProdutoCreateView(CreateView):
    model = models.Produto
    template_name = 'produto_create.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')


class ProdutoDetailView(DetailView):
    model = models.Produto
    template_name = 'produto_detail.html'


class ProdutoUpdateView(UpdateView):
    model = models.Produto
    template_name = 'produto_update.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')


class ProdutoDeleteView(DeleteView):
    model = models.Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produto_list')
