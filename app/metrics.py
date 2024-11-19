from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from marcas.models import Marca
from categorias.models import Categoria
from produtos.models import Produto
from saidas.models import Saida


def get_produto_metrics():
    produtos = Produto.objects.all()
    total_cost_price = sum(produto.cost_price * produto.quantity for produto in produtos)
    total_selling_price = sum(produto.selling_price * produto.quantity for produto in produtos)
    total_quantity = sum(produto.quantity for produto in produtos)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    total_sales = Saida.objects.count()
    total_produtos_sold = Saida.objects.aggregate(total_produtos_sold=Sum('quantity'))['total_produtos_sold'] or 0
    total_sales_value = sum(saidas.quantity * saidas.produto.selling_price for saidas in Saida.objects.all())
    total_sales_cost = sum(saidas.quantity * saidas.produto.cost_price for saidas in Saida.objects.all())
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_produtos_sold,
        total_sales_value=number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Saida.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('produto__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Saida.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(
        dates=dates,
        values=quantities,
    )


def get_graphic_produto_categoria_metric():
    categorias = Categoria.objects.all()
    return {categoria.name: Produto.objects.filter(categoria=categoria).count() for categoria in categorias}


def get_graphic_produto_marca_metric():
    marcas = Marca.objects.all()
    return {marca.name: Produto.objects.filter(marca=marca).count() for marca in marcas}