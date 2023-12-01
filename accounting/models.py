from django.db import models
from django.contrib.auth.models import User


import datetime

from company.models import Company
from employee.models import Employee
# Create your models here.


class GroupLedger(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    gl_no=models.IntegerField()
    gl_description=models.CharField(max_length=200)
    if_balance_sheet=models.BooleanField(default=False)
    if_profit_loss=models.BooleanField(default=False)
    if_trade_ac=models.BooleanField(default=False)
    if_not_balance_sheet=models.BooleanField(default=False)
    if_current_finyear=models.BooleanField(default=False)
    if_individual=models.BooleanField(default=False)
    if_consolidate_in_tb=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gl_description

class SubLedger(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    group_ledger=models.ForeignKey(GroupLedger,on_delete=models.PROTECT)
    sl_no=models.IntegerField()
    sl_description=models.CharField(max_length=200)
    remark=models.CharField(max_length=200,blank=True,null=True)
    ob_amount=models.DecimalField(decimal_places=2, max_digits=15,blank=True,null=True)
    ob_date=models.DateTimeField() # auto_now_add=True
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sl_description


class Daybook(models.Model):
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    js_number=models.IntegerField()
    js_date=models.DateField(default=datetime.date.today)
    js_description=models.CharField(max_length=200)
    manual_voucher_no=models.CharField(max_length=200,null=True,blank=True)
    if_manual_entry=models.BooleanField(default=False)
    credit_sl=models.ForeignKey(SubLedger,on_delete=models.PROTECT,related_name="credit")
    debit_sl=models.ForeignKey(SubLedger,on_delete=models.PROTECT,related_name="debit")
    js_amount=models.DecimalField(decimal_places=2, max_digits=15)
    if_multiple_journal=models.BooleanField(default=False)
    ref_number=models.IntegerField(null=True,blank=True)
    multiple_journal_no=models.IntegerField(null=True,blank=True)
    employee=models.ForeignKey(Employee,on_delete=models.PROTECT,null=True,blank=True)
    transaction_type=models.CharField(max_length=10,blank=True,null=True)
    bank_book_no=models.IntegerField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.js_description


class BankBook(models.Model):
    TRANSACTION_TYPE=(("RECEIPT","RECEIPT"),("PAYMENT","PAYMENT"))
    STATUS=(("PENDING","PENDING"),("PASSED","PASSED"),("BOUNCED","BOUNCED"),("CANCELLED","CANCELLED"))
    company=models.ForeignKey(Company,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    bank_book_code=models.IntegerField()
    reg_date=models.DateField(default=datetime.date.today)
    if_cash=models.BooleanField(default=False)
    bank_sl=models.ForeignKey(SubLedger,on_delete=models.PROTECT,related_name="banksl")
    cheque_no=models.CharField(max_length=200,null=True,blank=True)
    cheque_date=models.DateField(default=datetime.date.today)
    bankbook_sl_no=models.ForeignKey(SubLedger,on_delete=models.PROTECT,related_name="bankbook")
    transaction_type=models.CharField(choices=TRANSACTION_TYPE, max_length=20,default='RECEIPT')
    cheque_amount=models.DecimalField(decimal_places=2, max_digits=15)
    status=models.CharField(choices=STATUS, max_length=20,default="PENDING")
    status_date=models.DateField(default=datetime.date.today)
    if_rtgs=models.BooleanField(default=False)
    cheque_name=models.CharField(max_length=200)
    bank_charge=models.DecimalField(decimal_places=2, max_digits=15)
    bounce_charge=models.DecimalField(decimal_places=2, max_digits=15)
    js_no1=models.ForeignKey(Daybook,on_delete=models.PROTECT,null=True,blank=True, related_name="first_transaction") #link of CASHBOOK  (first transaction)
    js_no2=models.ForeignKey(Daybook,on_delete=models.PROTECT,null=True,blank=True, related_name="bank_charge") #link of CASHBOOK  (if bank charge is there)
    js_no3=models.ForeignKey(Daybook,on_delete=models.PROTECT,null=True,blank=True, related_name="bounced") #link of CASHBOOK (if bounced)
    js_no4=models.ForeignKey(Daybook,on_delete=models.PROTECT,null=True,blank=True, related_name="bounce_charge") #link of CASHBOOK (if bounce charge is there)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bank_book_code




