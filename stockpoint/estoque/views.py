from django.shortcuts import render
from django.urls import reverse
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .models import Estoque, EstoqueItens
from .forms import EstoqueItensForm, EstoqueForm

def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)

def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()  # cria uma nova instância de Estoque
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            # Salva o formulário principal
            estoque = form.save()
            # Salva os itens do estoque (formset)
            formset.save()
            # Redireciona para a página de detalhes do estoque
            return HttpResponseRedirect(reverse('estoque:estoque_entrada_detail', args=[estoque.pk]))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)

