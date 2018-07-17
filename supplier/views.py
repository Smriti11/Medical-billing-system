from django.shortcuts import render
from .models import Supplier
from django.http import HttpResponse
from .forms import AddSupplierForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required (login_url = '/login/')
def supplier(request):
    context={
    'supplier':Supplier.objects.all()
    }
    return render(request,'supplier.html',context)

@login_required (login_url = '/login/')
def supplier_update(request,id):
    supplier= Supplier.objects.get(pk=id)
    form = AddSupplierForm(request.POST or None,instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier')
    context = {
    'form':form,
    }
    return render(request,'supplier_update.html',context)

@login_required (login_url = '/login/')
def addsupplier(request):
   if request.method=="GET":
       context={
       'form':AddSupplierForm(),
       }
       return render(request,'addsupplier.html',context)
   else:
       form = AddSupplierForm(request.POST)
       if form.is_valid():
           sup = form.save(commit= True)
           sup.save()
           return redirect('supplier')
       else:
           return render(request,'addsupplier.html',{'form':form})


@login_required (login_url = '/login/')
def supplier_delete(request,id):
    try:
        supplier=Supplier.objects.get(pk=id)
        supplier.delete()
        return redirect('supplier')
    except:
        return redirect('supplier')
