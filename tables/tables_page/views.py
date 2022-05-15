from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Table
from tables.settings import QUANTITY


def pagina(request, table):
    paginator = Paginator(table, QUANTITY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def tables_view(request):
    tables = Table.objects.all()
    context = {
        'page_obj': pagina(request, tables),
    }
    return render(request, 'base.html', context)
