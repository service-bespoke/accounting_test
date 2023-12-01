from django.db import models

from company.models import *
from employee.models import *
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_PROFILE_THUMB="default.png"


class Permission(models.Model):
    name=models.CharField(max_length=70, null=False, blank=False) 
    
    def __str__(self):
        return self.name
    
class LoginCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    company=models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username
    

class UserPermission(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    staff = models.OneToOneField(Employee, on_delete=models.PROTECT,null=True)
    thumb = models.ImageField(null=True,blank=True,default=DEFAULT_PROFILE_THUMB)
    company=models.ManyToManyField(Company)
    permission=models.ManyToManyField(Permission)

    def permission_list(self):
        permission_list = list(set([x.name for x in self.permission.all()]))
        return permission_list
    


class Notifications(models.Model):
    company= models.ForeignKey(Company,on_delete=models.PROTECT)
    user= models.ForeignKey(User,on_delete=models.PROTECT)
    date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=500)