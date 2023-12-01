from django.urls import path
from . import views


app_name = 'masters'

urlpatterns = [
    path('customer/customerlist', views.customer, name='customerlist'),
    path('customer/create', views.customer_create, name='customer_create'),
]
