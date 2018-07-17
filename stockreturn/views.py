from django.shortcuts import render
from .models import Stockreturn

def stockreturn(request):
    context={
    'stockreturn':Stockreturn.objects.all()
    }
    return render(request,'stockreturn.html',context)
