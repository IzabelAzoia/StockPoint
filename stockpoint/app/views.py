import json
from django.shortcuts import render
from . import metrics


def home(request):
    produto_metrics = metrics.get_produto_metrics()
    sales_metrics = metrics.get_sales_metrics()
    graphic_produto_categoria_metric = metrics.get_graphic_produto_categoria_metric()
    graphic_produto_marca_metric = metrics.get_graphic_produto_marca_metric()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()

    context = {
        'produto_metrics': produto_metrics,
        'sales_metrics': sales_metrics,
        'produto_count_by_category': json.dumps(graphic_produto_categoria_metric),
        'produto_count_by_marca': json.dumps(graphic_produto_marca_metric),
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data)
    }

    return render(request, 'home.html', context)