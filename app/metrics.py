from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone


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
