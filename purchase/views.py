from django.shortcuts import render
from .models import Purchase
from django.http import HttpResponse
from django.shortcuts import redirect


def purchase(request):
    context={
    'purchase':Purchase.objects.all()
    }
    return render(request,'purchase.html',context)

def purchase_update(request):
    context={
    'purchase_update':Purchase.objects.get(id=id)
    }
    return render(request,'purchase_update.html',context)

def purchase_delete(request,id):
    try:
        purchase_delete= get_Purchase_or_404(Model, pk=purchase_id)
        purchase.delete()
        return redirect('purchase')
    except:
        return redirect('purchase')
