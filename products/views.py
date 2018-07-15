from django.shortcuts import render,redirect
from .models import Products
# Create your views here.
def products(request):
    context={
    'products':Products.objects.all()
    }
    return render(request,'products.html',context)

def pos(request):
    return render(request,'pos.html')
