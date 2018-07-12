from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Supplier
from .tables import SupplyTable

def supplier(request):
    table = SupplyTable(Supplier.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'supplier.html', {'table': table})
