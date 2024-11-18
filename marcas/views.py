from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class MarcaListView(ListView):
    model = models.Marca
    template_name = 'marca_list.html'
    context_object_name = 'marcas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class MarcaCreateView(CreateView):
    model = models.Marca
    template_name = 'marca_create.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')


class MarcaDetailView(DetailView):
    model = models.Marca
    template_name = 'marca_detail.html'


class MarcaUpdateView(UpdateView):
    model = models.Marca
    template_name = 'marca_update.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')


class MarcaDeleteView(DeleteView):
    model = models.Marca
    template_name = 'marca_delete.html'
    success_url = reverse_lazy('marca_list')

