from django.urls import path
from . import views
app_name = 'sales'
urlpatterns = [

    path('sales/create', views.createSales, name='create_sales'),

                
    path('get_customer_json', views.get_customers_json, name='get_customer_json'),
]
