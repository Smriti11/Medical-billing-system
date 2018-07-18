from django.shortcuts import render
from .models import Stockreturn
from django.http import HttpResponse
from .forms import AddStockreturnForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required (login_url = '/login/')
def stockreturn(request):
    context={
    'stockreturn':Stockreturn.objects.all()
    }
    return render(request,'stockreturn.html',context)

@login_required (login_url = '/login/')
def stockreturn_update(request,id):
    stockreturn= Stockreturn.objects.get(pk=id)
    form = AddStockreturnForm(request.POST or None,instance=stockreturn)
    if form.is_valid():
        form.save()
        return redirect('stockreturn')
    context = {
    'form':form,
    }
    return render(request,'stockreturn_update.html',context)

@login_required (login_url = '/login/')
def addstockreturn(request):
   if request.method=="GET":
       context={
       'form':AddStockreturnForm(),
       }
       return render(request,'addstockreturn.html',context)
   else:
       form = AddStockreturnForm(request.POST)
       if form.is_valid():
           sto = form.save(commit= True)
           sto.save()
           return redirect('stockreturn')
       else:
           return render(request,'addstockreturn.html',{'form':form})

@login_required (login_url = '/login/')
def stockreturn_delete(request,id):
    try:
        stockreturn=Stockreturn.objects.get(pk=id)
        stockreturn.delete()
        return redirect('stockreturn')
    except:
        return redirect('stockreturn')
