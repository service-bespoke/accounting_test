from django.urls import path
from . import views
#import pdb; pdb.set_trace()

app_name = 'accounting'
urlpatterns = [

    path('group_ledger/view_all', views.groupLedger, name='group_ledger_all'),
    path('group_ledger/<int:pk>/edit', views.glEdit, name='gl_edit'),
    path('group_ledger/<int:pk>/delete', views.glDelete, name='gl_delete'),

    
    path('sub_ledger/view_all', views.subLedger, name='sub_ledger_all'),
    path('sub_ledger/<int:pk>/edit', views.slEdit, name='sl_edit'),
    path('sub_ledger/<int:pk>/delete', views.slDelete, name='sl_delete'),

    path('cash_receipt/view_all', views.cashReceipt, name='cash_receipt_all'),  
    path('cash_receipt/<int:pk>/edit', views.crEdit, name='cr_edit'),
    path('cash_receipt/<int:pk>/delete', views.crDelete, name='cr_delete'),

    path('cash_payment/view_all', views.cashPayment, name='cash_payment_all'),  
    path('cash_payment/<int:pk>/edit', views.cpEdit, name='cp_edit'),
    path('cash_payment/<int:pk>/delete', views.cpDelete, name='cp_delete'), 

    path('journal_entry/view_all', views.journalEntry, name='journal_entry_all'),  
    path('journal_entry/<int:pk>/edit', views.jeEdit, name='je_edit'),
    path('journal_entry/<int:pk>/delete', views.jeDelete, name='je_delete'),

     
    path('cheque_register/view_all', views.chequeRegister, name='cheque_register_all'),  

    path('cash_book/view_all', views.cashBook, name='cash_book'),  
]
