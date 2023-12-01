from django.shortcuts import redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib import messages

from django.db.models import Max
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from users.views import getLoginCompany

from .models import *
from .forms import *
from datetime import datetime, timedelta
from django.db.models import Q

from django.core.exceptions import ObjectDoesNotExist



def create_daybook(js_data):
    js_no=Daybook.objects.filter(company=js_data['company']).aggregate(Max('js_number'))['js_number__max']
    if js_no:
        js_no+=1
    else:
        js_no=1
    credit_sl=SubLedger.objects.get(company=js_data['company'],sl_no=js_data['credit_sl'])
    debit_sl=SubLedger.objects.get(company=js_data['company'],sl_no=js_data['debit_sl'])
    sl_object=Daybook(company=js_data['company'],
                        user=js_data['user'],
                        js_number=js_no,
                        js_date=js_data['date'],
                        js_description=js_data["description"],
                        manual_voucher_no=js_data["voucher_no"],
                        if_manual_entry=js_data["is_manual"],
                        credit_sl=credit_sl,
                        debit_sl=debit_sl,
                        js_amount=js_data["amount"],
                        if_multiple_journal=js_data["is_multiple"],
                        ref_number=js_data["ref_number"],
                        multiple_journal_no=js_data["multiple_journal_no"],
                        employee=js_data["employee"],
                        bank_book_no=js_data["bank_book_no"])
    sl_object.save()

    return sl_object


def groupLedger(request):
    context={}
    company=getLoginCompany(request.user)
    group_ledger = GroupLedger.objects.filter(company=company).order_by('-id')
    glForm=GroupLedgerForm
    context['glForm']=glForm
    context['group_ledger']=group_ledger
    context['gl_no'] = GroupLedger.objects.filter(company=company).aggregate(Max('gl_no'))['gl_no__max']
    if not context['gl_no']:
        context['gl_no'] = 1001
    else:
        context['gl_no'] += 1
    if request.method=='POST':
        glForm = GroupLedgerForm(request.POST)
        if glForm.is_valid():
            gl_instance = glForm.save(commit=False)
            gl_instance.user=request.user
            gl_instance.gl_no=context['gl_no']
            gl_instance.company=company
            gl_instance.save()
            glForm.save_m2m()
            context['gl_no'] = GroupLedger.objects.filter(company=company).aggregate(Max('gl_no'))['gl_no__max']
        else:
            context['glForm']=glForm
            return render(request,'groupLedger/index.html',context)
        return render(request,'groupLedger/index.html',context)
    return render(request,'groupLedger/index.html',context)


def glEdit(request,pk):
    company=getLoginCompany(request.user)
    context={}
    group_ledger = GroupLedger.objects.get(id=pk)
    group_ledgers = GroupLedger.objects.filter(company=company).order_by('-id')
    glForm=GroupLedgerForm(request.POST or None, instance=group_ledger)
    context['glForm']=glForm
    context['group_ledger']=group_ledgers
    context['gl_no'] =group_ledger.gl_no
    if request.method== 'POST':
        if glForm.is_valid():
            glForm.save()
            return redirect('accounting:group_ledger_all')
    return render(request,'groupLedger/index.html',context)


def glDelete(request,pk):
    try:
        GroupLedger.objects.get(id=pk).delete()
        messages.success(request, "Group Ledger Successfully deleted!!" )
    except ProtectedError:
        messages.error(request, "Group Ledger can't be deleted!!" )
    return redirect('accounting:group_ledger_all')






## SubLedger Started ---------------------  ##





def subLedger(request):
    context={}
    company=getLoginCompany(request.user)
    sub_ledger = SubLedger.objects.filter(company=company).order_by('-id')
    slForm=SubLedgerForm
    context['slForm']=slForm
    context['sub_ledger']=sub_ledger
    context['sl_no'] = SubLedger.objects.aggregate(Max('sl_no'))['sl_no__max']
    if not context['sl_no']:
        context['sl_no'] = 1000
    else:
        context['sl_no'] += 1
    if request.method=='POST':
        slForm = SubLedgerForm(request.POST)
 
        if slForm.is_valid():
            sl_instance = slForm.save(commit=False)
            sl_instance.user=request.user
            sl_instance.sl_no=context['sl_no']
            sl_instance.company=company
            sl_instance.save()
            slForm.save_m2m()
            context['sl_no'] = SubLedger.objects.aggregate(Max('sl_no'))['sl_no__max']
        else:
            context['slForm']=slForm
            return render(request,'subLedger/index.html',context)
        return render(request,'subLedger/index.html',context)
    return render(request,'subLedger/index.html',context)



def slEdit(request,pk):
    company=getLoginCompany(request.user)
    context={}
    sub_ledger = SubLedger.objects.get(id=pk)
    sub_ledgers = SubLedger.objects.filter(company=company).order_by('-id')
    slForm=SubLedgerForm(request.POST or None, instance=sub_ledger)

    context['slForm']=slForm
    context['sub_ledger']=sub_ledgers
    context['sl_no'] =sub_ledger.sl_no

    if request.method == 'POST':
        if slForm.is_valid():
            slForm.save()
            messages.error(request, "Sub Ledger updated!!" )
            return redirect('accounting:sub_ledger_all')
    return render(request,'subLedger/index.html',context)


def slDelete(request,pk):
    try:
        SubLedger.objects.get(id=pk).delete()
        messages.success(request, "Sub Ledger Successfully deleted!!" )
    except ProtectedError:
        messages.error(request, "Sub Ledger can't be deleted!!" )
    return redirect('accounting:sub_ledger_all')



## Cash Receipt -------------------- ##


def cashReceipt(request):
    context={}
    company=getLoginCompany(request.user)
    transaction_type='R'
    cash_sl_no=1000
    cash_book = Daybook.objects.filter(company=company,transaction_type=transaction_type).order_by('-id')
    receiptForm=CashReceiptForm
    context['crForm']=receiptForm
    context['cash_book']=cash_book
    context['cr_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
    head_name =  SubLedger.objects.get(company=company,sl_no=1000)


    if not context['cr_no']:
        context['cr_no'] = 1100
    else:
        context['cr_no'] += 1
    if request.method=='POST':
        receiptForm = CashReceiptForm(request.POST)
        if receiptForm.is_valid():
            cr_instance = receiptForm.save(commit=False)
            cr_instance.user=request.user
            cr_instance.js_number=context['cr_no']
            cr_instance.company=company
            cr_instance.transaction_type=transaction_type
            cr_instance.debit_sl=head_name
            cr_instance.save()
            receiptForm.save_m2m()
            context['cr_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
        else:
            context['crForm']=receiptForm
            return render(request,'cashReceipt/index.html',context)
        return render(request,'cashReceipt/index.html',context)
    return render(request,'cashReceipt/index.html',context)


def crEdit(request,pk):
    company=getLoginCompany(request.user)
    context={}
    cash_receipt = Daybook.objects.get(id=pk)
    cash_receipt_all = Daybook.objects.filter(company=company).order_by('-id')
    crForm=CashReceiptForm(request.POST or None, instance=cash_receipt)

    context['crForm']=crForm
    context['cash_receipt_all']=cash_receipt_all
    context['js_number'] =cash_receipt.js_number

    if request.method == 'POST':
        if crForm.is_valid():
            crForm.save()
            messages.error(request, "Cash Receipt updated!!" )
            return redirect('accounting:cash_receipt_all')
    return render(request,'cashReceipt/index.html',context)


def crDelete(request,pk):
    try:
        Daybook.objects.get(id=pk).delete()
        messages.success(request, "Cash Receipt Successfully deleted!!" )
    except ProtectedError:
        messages.error(request, "Cash Receipt can't be deleted!!" )
    return redirect('accounting:cash_receipt_all')


def cashPayment(request):
    context={}
    company=getLoginCompany(request.user)
    transaction_type='P'
    cash_sl_no='1000'
    cash_book = Daybook.objects.filter(company=company,transaction_type=transaction_type).order_by('-id')
    paymentForm=CashPaymentForm
    context['cpForm']=paymentForm
    context['cash_book']=cash_book
    head_name =  SubLedger.objects.get(company=company,sl_no=1000)
    
    context['cp_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
    if not context['cp_no']:
        context['cp_no'] = 1100
    else:
        context['cp_no'] += 1
    if request.method=='POST':
        paymentForm = CashPaymentForm(request.POST)
        if paymentForm.is_valid():
            cp_instance = paymentForm.save(commit=False)
            cp_instance.user=request.user
            cp_instance.js_number=context['cp_no']
            cp_instance.company=company
            cp_instance.transaction_type=transaction_type
            cp_instance.credit_sl=head_name
            cp_instance.save()
            paymentForm.save_m2m()
            context['cp_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
        else:
            context['cpForm']=paymentForm
            return render(request,'cashPayment/index.html',context)
        return render(request,'cashPayment/index.html',context)
    return render(request,'cashPayment/index.html',context)


def cpEdit(request,pk):
    company=getLoginCompany(request.user)
    context={}
    cash_payment = Daybook.objects.get(id=pk)
    cash_payment_all = Daybook.objects.filter(company=company).order_by('-id')
    cpForm=CashPaymentForm(request.POST or None, instance=cash_payment)

    context['cpForm']=cpForm
    context['cash_payment_all']=cash_payment_all
    context['js_number'] =cash_payment.js_number

    if request.method == 'POST':
        if cpForm.is_valid():
            cpForm.save()
            messages.error(request, "Cash Payment updated!!" )
            return redirect('accounting:cash_payment_all')
    return render(request,'cashPayment/index.html',context)


def cpDelete(request,pk):
    try:
        Daybook.objects.get(id=pk).delete()
        messages.success(request, "Cash Payment Successfully deleted!!" )
    except ProtectedError:
        messages.error(request, "Cash Payment can't be deleted!!" )
    return redirect('accounting:cash_payment_all')

## Journal Entry ---------------------- ##

def journalEntry(request):
    context={}
    company=getLoginCompany(request.user)
    cash_book = Daybook.objects.filter(company=company).order_by('-id')
    journalForm=JournalEntryForm
    context['jeForm']=journalForm
    context['cash_book']=cash_book
    
    context['je_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
    if not context['je_no']:
        context['je_no'] = 1100
    else:
        context['je_no'] += 1
    if request.method=='POST':
        journalForm = JournalEntryForm(request.POST)
        
        # Credit = journalForm.post('credit_sl')
        # Debit = journalForm.post('debit_sl')
        # if Credit and Debit and Credit == Debit:
        #     messages.error(request, "Debit and Credit must be different!!" )
        #     return redirect('accounting:journal_entry_all')

        if journalForm.is_valid():
            je_instance = journalForm.save(commit=False)
            je_instance.user=request.user
            je_instance.js_number=context['je_no']
            je_instance.company=company
            je_instance.save()
            journalForm.save_m2m()
            context['je_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
        else:
            context['jeForm']=journalForm
            messages.error(request, "Ledger Account Head must be different.!!" )
           # return redirect('accounting:journal_entry_all')
            return render(request,'journalEntry/index.html',context)
        return render(request,'journalEntry/index.html',context)
    return render(request,'journalEntry/index.html',context)



def jeEdit(request,pk):
    company=getLoginCompany(request.user)
    context={}
    journal_entry = Daybook.objects.get(id=pk)
    journal_entry_all = Daybook.objects.filter(company=company).order_by('-id')
    jeForm=JournalEntryForm(request.POST or None, instance=journal_entry)

    context['jeForm']=jeForm
    context['journal_entry_all']=journal_entry_all
    context['js_number'] =journal_entry.js_number

    if request.method == 'POST':
        if jeForm.is_valid():
            jeForm.save()
            messages.error(request, "Journal Entry updated!!" )
            return redirect('accounting:journal_entry_all')
    return render(request,'journalEntry/index.html',context)


def jeDelete(request,pk):
    try:
        Daybook.objects.get(id=pk).delete()
        messages.success(request, "Journal Entry Successfully deleted!!" )
    except ProtectedError:
        messages.error(request, "Journal Entry can't be deleted!!" )
    return redirect('accounting:journal_entry_all')




## Cash Book -------------------- ##


# def cashBookTry(request):
#     context={}
#     company=getLoginCompany(request.user)

#     journal_entries = Daybook.objects.filter(company=company)
#     return render(request, 'cashbook/journal_entry_statement.html', {'journal_entries': journal_entries})


def cashBook(request):
    context={}
    company=getLoginCompany(request.user)
    income_entries = 0
    expense_entries = 0
    total_income = 0
    total_expense = 0
    net_cash_flow = 0
    sdate = 0
    edate = 0
    journal_entries = 0


    if request.method=='POST':
        sdate = request.POST.get('from')
        edate = request.POST.get('to')

        journal_entries = Daybook.objects.filter(company=company,js_date__range=[sdate, edate])
        income_entries = Daybook.objects.filter(
            company=company,
            transaction_type='R',
            js_date__range=[sdate, edate]
        )

      
        expense_entries = Daybook.objects.filter(
            company=company,
            transaction_type='P',
            js_date__range=[sdate, edate]
        )

        total_income = income_entries.aggregate(total=models.Sum('js_amount'))['total'] or 0
        total_expense = expense_entries.aggregate(total=models.Sum('js_amount'))['total'] or 0

        net_cash_flow = total_income - total_expense

    else:
        context['cash_book'] = Daybook.objects.filter(company=company).order_by('-id')
        return render(
        request,
        'cashbook/index.html',
        {
            'income_entries': income_entries,
            'expense_entries': expense_entries,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_cash_flow': net_cash_flow,
            'journal_entries': journal_entries,
            'start_date' : sdate,
            'end_date' : edate,
          
        }
    )
    return render(
        request,
        'cashbook/index.html',
        {
           'income_entries': income_entries,
            'expense_entries': expense_entries,
            'total_income': total_income,
            'total_expense': total_expense,
            'net_cash_flow': net_cash_flow,
            'journal_entries': journal_entries,
            'start_date' : sdate,
            'end_date' : edate
          
        }
    )


## Cheque Register -------------------- ##


def chequeRegister(request):
    context={}
    company=getLoginCompany(request.user)
    transaction_type='R'
    cash_sl_no=1000
    cash_book = Daybook.objects.filter(company=company,transaction_type=transaction_type).order_by('-id')
    receiptForm=CashReceiptForm
    context['crForm']=receiptForm
    context['cash_book']=cash_book
    context['cr_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
    head_name =  SubLedger.objects.get(company=company,sl_no=1000)


    if not context['cr_no']:
        context['cr_no'] = 1100
    else:
        context['cr_no'] += 1
    if request.method=='POST':
        receiptForm = CashReceiptForm(request.POST)
        if receiptForm.is_valid():
            cr_instance = receiptForm.save(commit=False)
            cr_instance.user=request.user
            cr_instance.js_number=context['cr_no']
            cr_instance.company=company
            cr_instance.transaction_type=transaction_type
            cr_instance.debit_sl=head_name
            cr_instance.save()
            receiptForm.save_m2m()
            context['cr_no'] = Daybook.objects.filter(company=company).aggregate(Max('js_number'))['js_number__max']
        else:
            context['crForm']=receiptForm
            return render(request,'chequeRegister/index.html',context)
        return render(request,'chequeRegister/index.html',context)
    return render(request,'chequeRegister/index.html',context)

