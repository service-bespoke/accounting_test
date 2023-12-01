from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([UserPermission,LoginCompany,Permission,Notifications])