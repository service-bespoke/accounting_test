from django.urls import path
from . import views
app_name = 'items'
urlpatterns = [

    path('view_all', views.viewItem, name='view_all_item'),
    path('create', views.createItem, name='create_item'),
    # path('group_ledger/edit', views.editItem, name='gl_edit'),

    path('get_item_json', views.get_item_json, name='get_item_json'),
    path('get_supplier_json', views.get_supplier_json, name='get_supplier_json'),

]
