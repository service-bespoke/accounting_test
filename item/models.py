from django.db import models

from company.models import Company

# Create your models here.

class Category(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Unit(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    unit=models.ForeignKey(Unit,on_delete=models.PROTECT)
    itemCode=models.CharField(max_length=200)
    itemName=models.CharField(max_length=200)
    description=models.CharField(max_length=500,null=True,blank=True)
    make=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    vat=models.DecimalField(default=0,decimal_places=2, max_digits=15)
    is_vatInclusive=models.BooleanField(default=True)

    def __str__(self):
        return self.itemName


class ItemBatch(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    item=models.ForeignKey(Item,on_delete=models.PROTECT)
    batch=models.CharField(max_length=200)
    sales_rate=models.DecimalField(default=0,decimal_places=2, max_digits=15)
    purchase_rate=models.DecimalField(default=0,decimal_places=2, max_digits=15)
    cost=models.DecimalField(default=0,decimal_places=2, max_digits=15)
    openingStock=models.IntegerField()
    currentStock=models.IntegerField()



