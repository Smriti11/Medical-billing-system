from django.shortcuts import render,redirect
from .models import Products
from .forms import AddProductsForm
# Create your views here.
def products(request):
    context={
    'products':Products.objects.all()
    }
    return render(request,'products.html',context)

def pos(request):
    return render(request,'pos.html')

def addproduct(request):
    if request.method=="GET":
        context={
        'form':AddProductsForm(),
        }
        return render(request,'addprod.html',context)
    else:
        form = AddProductsForm(request.POST)
        if form.is_valid():
            prod = form.save(commit= True)
            prod.save()
            return redirect('products')
        else:
            return render(request,'addprod.html',{'form':form})
