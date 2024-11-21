from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class CategoriaListView(ListView):
    model = models.Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoriaCreateView(CreateView):
    model = models.Categoria
    template_name = 'categoria_create.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')


class CategoriaDetailView(DetailView):
    model = models.Categoria
    template_name = 'categoria_detail.html'


class CategoriaUpdateView(UpdateView):
    model = models.Categoria
    template_name = 'categoria_update.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(DeleteView):
    model = models.Categoria
    template_name = 'categoria_delete.html'
    success_url = reverse_lazy('categoria_list')