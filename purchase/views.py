
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Purchase
from .tables import PurchaseTable
from django.http import HttpResponse

def purchase(request):
    table = PurchaseTable(Purchase.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'purchase.html', {'table': table})


def purchase_update(request,id):
    purchase=Purchase.objects.get(id=id)
    return render(request, 'purchase_update.html', {'table': table})
- 
