from django.shortcuts import render,redirect
<<<<<<< HEAD
from .models import Products
# Create your views here.
def products(request):
    context={
    'products':Products.objects.all()
    }
    return render(request,'products.html',context)
=======
from django_tables2 import RequestConfig
from .tables import ProductTable
from .models import Products
# Create your views here.
def products(request):
    table = ProductTable(Products.objects.all())
    RequestConfig(request).configure(table)
    return render(request,'products.html',{'table':table})
>>>>>>> 3dab086088074a8709f3e30114718087c3d24e78
