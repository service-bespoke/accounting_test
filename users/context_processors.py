
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
import datetime
from django.db.models import Q,Sum

from .models import *


def get_company(request):
    if request.user.is_authenticated:
        if LoginCompany.objects.filter(user=request.user).exists():
            if UserPermission.objects.filter(user=request.user).exists():
                login_company=LoginCompany.objects.get(user=request.user)
                user_details=UserPermission.objects.get(user=request.user)
                company=login_company.company
            else:
                company=None
                user_details=None
        else:
            company=None
            user_details=None
    else:
        company =None
        user_details=None
    return { 'company':company,'user_details':user_details}




def get_permission_list(request):
    if request.user.is_authenticated :
        if UserPermission.objects.filter(user=request.user).exists():
            profile=UserPermission.objects.get(user=request.user)
            permissions=[]
            for permission in profile.permission.all():
                permissions.append(permission.name)
        else:
            permissions=[]
    else:
        permissions=[]
    return {'permissions':permissions}



