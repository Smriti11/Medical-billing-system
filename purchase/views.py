from django.shortcuts import render
from .models import Purchase
from django.http import HttpResponse
from .forms import AddPurchaseForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required (login_url = '/login/')
def purchase(request):
    context={
    'purchase_':Purchase.objects.all()
    }
    return render(request,'purchase.html',context)

@login_required (login_url = '/login/')
def addpurchase(request):
   if request.method=="GET":
       context={
       'form':AddPurchaseForm(),
       }
       return render(request,'addpurchase.html',context)
   else:
       form = AddPurchaseForm(request.POST)
       if form.is_valid():
           pur = form.save(commit= True)
           pur.save()
           return redirect('purchase')
       else:
           return render(request,'addpurchase.html',{'form':form})

@login_required (login_url = '/login/')
def purchase_update(request,id):
    purchase= Purchase.objects.get(pk=id)
    form = AddPurchaseForm(request.POST or None,instance=purchase)
    if form.is_valid():
        form.save()
        return redirect('purchase')
    context = {
    'form':form,
    }
    return render(request,'purchase_update.html',context)

@login_required (login_url = '/login/')
def purchase_delete(request,id):
    try:
        purchase= Purchase.objects.get(pk=id)
        purchase.delete()
        return redirect('purchase')
    except:
        return redirect('purchase')
