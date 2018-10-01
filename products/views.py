from django.shortcuts import render,redirect
from .models import Products
from .forms import AddProductsForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required (login_url = '/login/')
def products(request):
    context={
    'products':Products.objects.all()
    }
    return render(request,'products.html',context)


@login_required (login_url = '/login/')
def addproduct(request):
   if request.method=="GET":
       context={
       'form':AddProductsForm(),
       }
       return render(request,'addprod.html',context)
   else:
       form = AddProductsForm(request.POST)
       if form.is_valid():
           p = form.save(commit= True)
           p.save()
           return redirect('products')
       else:
           return render(request,'addprod.html',{'form':form})

@login_required (login_url = '/login/')
def products_update(request,id):
    products= Products.objects.get(pk=id)
    form = AddProductsForm(request.POST or None,instance=products)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {
    'form':form,
    }
    return render(request,'product_update.html',context)

@login_required (login_url = '/login/')
def products_delete(request,id):
    try:
        products=Products.objects.get(pk=id)
        products.delete()
        return redirect('products')
    except:
        return redirect('products')
