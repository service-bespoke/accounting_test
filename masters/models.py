from django.db import models

from django.db import models
from django.contrib.auth.models import User


import datetime

from company.models import Company
from employee.models import Employee
# Create your models here.


class Customer(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer_code=models.IntegerField()
    customer_name=models.CharField(max_length=200)
    customer_address1=models.CharField(max_length=200,blank=True,null=True)
    customer_address2=models.CharField(max_length=200,blank=True,null=True)
    customer_address3=models.CharField(max_length=200,blank=True,null=True)
    customer_phone1=models.CharField(max_length=200,blank=True,null=True)
    customer_phone2=models.CharField(max_length=200,blank=True,null=True)
    customer_email=models.EmailField(max_length=125,blank=True,null=True)
    customer_trn=models.CharField(max_length=20,blank=True,null=True)
    customer_slno=models.IntegerField()
    customer_ob_amount=models.DecimalField(decimal_places=2, max_digits=15,blank=True,null=True)
    customer_ob_date=models.DateField(blank=True,null=True)
    created_time=models.DateTimeField(auto_now_add=True)

class Supplier(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    supplier_code=models.IntegerField()
    supplier_name=models.CharField(max_length=200)
    supplier_address1=models.CharField(max_length=200,blank=True,null=True)
    supplier_address2=models.CharField(max_length=200,blank=True,null=True)
    supplier_address3=models.CharField(max_length=200,blank=True,null=True)
    supplier_phone1=models.CharField(max_length=200,blank=True,null=True)
    supplier_phone2=models.CharField(max_length=200,blank=True,null=True)
    supplier_email=models.EmailField(blank=True,null=True)
    supplier_trn=models.CharField(max_length=20,blank=True,null=True)
    supplier_slno=models.IntegerField()
    supplier_ob_amount=models.DecimalField(decimal_places=2, max_digits=15)
    supplier_ob_date=models.DateTimeField(auto_now_add=True)
    created_time=models.DateTimeField(auto_now_add=True)

class Bank(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bank_code=models.IntegerField()
    bank_name=models.CharField(max_length=200)
    bank_branch=models.CharField(max_length=200)
    bank_accountno=models.CharField(max_length=20)
    bank_iban=models.CharField(max_length=30)
    bank_slno=models.IntegerField()
    bank_ob_amount=models.DecimalField(decimal_places=2, max_digits=15)
    bank_ob_date=models.DateTimeField(auto_now_add=True)
    created_time=models.DateTimeField(auto_now_add=True)