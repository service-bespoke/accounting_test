
from django.http import JsonResponse
from django.shortcuts import render
from masters.forms import CustomerForm
from masters.models import Customer
from django.db.models import Max
from users.views import getLoginCompany
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def customer(request):
    custdetails = Customer.objects.all()
    context ={
        'custdetails':custdetails
    }
    return render(request,'customer/index.html',context)

def customer_create(request):
    context={}
    company=getLoginCompany(request.user)
    custForm=CustomerForm
    context['custForm']=CustomerForm
    context['customer_code'] = Customer.objects.filter(company=company).aggregate(Max('customer_code'))['customer_code__max']
    if not context['customer_code']:
        context['customer_code'] = 1
    else:
        context['customer_code'] += 1

    context['customer_slno'] = Customer.objects.filter(company=company).aggregate(Max('customer_slno'))['customer_slno__max']
    if not context['customer_slno']:
        context['customer_slno'] = 500001
    else:
        context['customer_slno'] += 1

    if request.method=='POST':
        custForm =CustomerForm(request.POST)
        if custForm.is_valid():
            cust_instance = custForm.save(commit=False)
            cust_instance.user=request.user
            cust_instance.company=company
            cust_instance.customer_code= context['customer_code']
            cust_instance.customer_slno=context['customer_slno']
            cust_instance.save()
            custForm.save()
        else:
            context['custForm']=custForm
            return render(request,'customer/create.html',context)
        return render(request,'customer/create.html',context)
    return render(request,'customer/create.html',context)





    