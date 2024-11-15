from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import CreateView, UpdateView


def produto_list(request):
    template_name = 'produto_list.html'
    produtos = Produto.objects.all()
    context = {'object_list': produtos}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    produto = get_object_or_404(Produto, pk=pk)
    context = {'object': produto}
    return render(request, template_name, context)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.object.get_absolute_url())


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.object.get_absolute_url())


def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    if produto.exists():
        data = [item.to_dict_json() for item in produto]
        return JsonResponse({'data': data})
    else:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

