from django.http import JsonResponse
from django.shortcuts import render
from masters.models import Customer

from users.views import getLoginCompany


def createSales(request):
    return render(request,'sales/create.html')

def get_customers_json(request):
    company=getLoginCompany(request.user)
    customers = list(Customer.objects.filter(company=company).values())
    return JsonResponse(customers, safe=False)