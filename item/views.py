from django.http import JsonResponse
from django.shortcuts import render
from item.forms import *
from item.models import *
from masters.models import Supplier

from users.views import getLoginCompany




def viewItem(request):
    company=getLoginCompany(request.user)
    context={}
    context['items']=Item.objects.filter(company=company)
    return render(request,'item/index.html',context)


def createItem(request):
    company=getLoginCompany(request.user)
    context={}
    context['batchForm']=ItemBatchForm
    context['itemForm']=ItemForm
    if request.method=='POST':
        item_data = request.POST
        if item_data['item_id']:
            item=Item.objects.get(id=item_data['item_id'])
        else:
            itemForm=ItemForm(request.POST)
            if itemForm.is_valid():
                item = itemForm.save(commit=False)
                item.company=company
                item.save()
                itemForm.save_m2m()
        batchForm=ItemBatchForm(request.POST)
        if batchForm.is_valid():
            batch_instance = batchForm.save(commit=False)
            batch_instance.item=item
            batch_instance.company=company
            batch_instance.batch=item_data['batch']
            batch_instance.currentStock=batch_instance.openingStock
            batch_instance.save()
            batchForm.save_m2m()
    return render(request,'item/create.html',context)



def get_item_json(request):
    company=getLoginCompany(request.user)
    items = list(Item.objects.filter(company=company).values())
    return JsonResponse(items, safe=False)


def get_supplier_json(request):
    company=getLoginCompany(request.user)
    suppliers = list(Supplier.objects.filter(company=company).values())
    return JsonResponse(suppliers, safe=False)