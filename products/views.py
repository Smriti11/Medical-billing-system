from django.shortcuts import render,redirect
from django_tables2 import RequestConfig
from .tables import ProductTable
from .models import Products
# Create your views here.
def products(request):
    table = ProductTable(Products.objects.all())
    RequestConfig(request).configure(table)
    return render(request,'products.html',{'table':table})
