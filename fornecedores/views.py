from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class FornecedorListView(ListView):
    model = models.Fornecedor
    template_name = 'fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class FornecedorCreateView(CreateView):
    model = models.Fornecedor
    template_name = 'fornecedor_create.html'
    form_class = forms.FornecedorForm
    success_url = reverse_lazy('fornecedor_list')


class FornecedorDetailView(DetailView):
    model = models.Fornecedor
    template_name = 'fornecedor_detail.html'
    context_object_name = 'object' 


class FornecedorUpdateView(UpdateView):
    model = models.Fornecedor
    template_name = 'fornecedor_update.html'
    form_class = forms.FornecedorForm
    success_url = reverse_lazy('fornecedor_list')


class FornecedorDeleteView(DeleteView):
    model = models.Fornecedor
    template_name = 'fornecedor_delete.html'
    success_url = reverse_lazy('fornecedor_list')