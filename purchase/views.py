
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Purchase
from .tables import PurchaseTable

def purchase(request):
    table = PurchaseTable(Purchase.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'purchase.html', {'table': table})
