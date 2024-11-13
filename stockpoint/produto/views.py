from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm

# Função para listar produtos
def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

# Função para visualizar o detalhe de um produto
def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    # Usando get_object_or_404 para evitar erro caso o produto não exista
    obj = get_object_or_404(Produto, pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

# CreateView para adicionar um novo produto
class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

    # Redireciona para a página de detalhes do produto após a criação
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.object.get_absolute_url())

# UpdateView para editar um produto existente
class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

    # Redireciona para a página de detalhes do produto após a atualização
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.object.get_absolute_url())
