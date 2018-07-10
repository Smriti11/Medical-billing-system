<<<<<<< HEAD
from django.shortcuts import render
from .models import Purchase

def purchase(request):
    context={
    'purchase':Purchase.objects.all()
    }
    return render(request,'purchase.html',context)
=======

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Purchase
from .tables import PurchaseTable

def purchase(request):
    table = PurchaseTable(Purchase.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'purchase.html', {'table': table})
>>>>>>> 3dab086088074a8709f3e30114718087c3d24e78
