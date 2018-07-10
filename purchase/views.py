from django.shortcuts import render
from .models import Purchase

def purchase(request):
    context={
    'purchase':Purchase.objects.all()
    }
    return render(request,'purchase.html',context)
