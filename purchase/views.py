from django.shortcuts import render,redirect
from .models import Purchase
from .forms import AddPurchaseForm

def purchase(request):
    context={
    'purchase':Purchase.objects.all()
    }
    return render(request,'purchase.html',context)

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

def purchase_update(request,id):
     if request.POST:
        form= AddPurchaseForm(request.POST)
        if form.is_valid():
            purchase = Purchase.objects.get(pk=id)
            form= AddPurchaseForm(request.POST or None,instance=purchase)
            form.save()
            return redirect('purchase')
        else:
            purchase = Purchase.objects.get(pk=id)
            form= AddPurchaseForm(instance=purchase)
            context={
            'form':form
            }
            return render(request,'purchase_update.html',context)
