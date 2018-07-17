from django.shortcuts import render
from .models import Supplier

def supplier(request):
    context={
    'supplier':Supplier.objects.all()
    }
    return render(request,'supplier.html',context)
