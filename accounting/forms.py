from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *

class GroupLedgerForm(forms.ModelForm):
    class Meta:
        model=GroupLedger
        fields=('gl_description','if_balance_sheet','if_profit_loss','if_trade_ac','if_not_balance_sheet','if_current_finyear','if_individual','if_consolidate_in_tb')
        widgets={
            'gl_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'if_balance_sheet': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_profit_loss': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_trade_ac': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_not_balance_sheet': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_current_finyear': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_individual': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'if_consolidate_in_tb': forms.CheckboxInput(attrs={'class':'form-check-input'}),
    }


class SubLedgerForm(forms.ModelForm):
    class Meta:
        model=SubLedger
        fields=('sl_description','group_ledger','remark','ob_amount','ob_date')
        widgets={
           'sl_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'group_ledger': forms.Select(attrs={'class':'form-select'}),
             'remark': forms.TextInput(attrs={'class':'form-control','placeholder':'Remark'}),
             'ob_amount': forms.TextInput(attrs={'class':'form-control','placeholder':'Amount'}),
             'ob_date': forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (ob_date)',
                'class': 'form-control'
                }),
     

    }
   
class CashReceiptForm(forms.ModelForm):

    credit_sl = forms.ModelChoiceField(
    queryset=SubLedger.objects.exclude(sl_no=1000), widget=forms.Select(attrs={'class':'form-select'}),
    empty_label="Select Sub Ledger"
)
        
    class Meta:
        model=Daybook
       # fields = "__all__"  
        exclude=['debit_sl']
        fields=('js_description','js_date','manual_voucher_no','if_manual_entry','credit_sl','js_amount')
        widgets={
           'js_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
           'js_date': forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (js_date)',
                'class': 'form-control'
                }),
           'manual_voucher_no': forms.TextInput(attrs={'class':'form-control','placeholder':'Voucher Number'}),
           'if_manual_entry': forms.CheckboxInput(attrs={'class':'form-check-input'}),
           'credit_sl': forms.Select(attrs={'class':'form-select'}),
           'js_amount': forms.TextInput(attrs={'class':'form-control','placeholder':'Amount'}),
       }
   
   
class CashPaymentForm(forms.ModelForm):

    debit_sl = forms.ModelChoiceField(
        queryset=SubLedger.objects.exclude(sl_no=1000), widget=forms.Select(attrs={'class':'form-select'}),
        empty_label="Select Sub Ledger"
    )
    class Meta:
        model=Daybook
        exclude=['credit_sl']
       # fields = "__all__"  
        fields=('js_description','js_date','manual_voucher_no','if_manual_entry','debit_sl','js_amount')
        widgets={
           'js_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
           'js_date': forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (js_date)',
                'class': 'form-control'
                }),
           'manual_voucher_no': forms.TextInput(attrs={'class':'form-control','placeholder':'Voucher Number'}),
           'if_manual_entry': forms.CheckboxInput(attrs={'class':'form-check-input'}),
           'debit_sl': forms.Select(attrs={'class':'form-select'}),
           'js_amount': forms.TextInput(attrs={'class':'form-control','placeholder':'Amount'}),
       }
   
class JournalEntryForm(forms.ModelForm):
    class Meta:
        model=Daybook
       # fields = "__all__"  
        fields=('js_description','js_date','manual_voucher_no','if_manual_entry','credit_sl','debit_sl','js_amount')
        widgets={
           'js_description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
           'js_date': forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (js_date)',
                'class': 'form-control'
                }),
           'manual_voucher_no': forms.TextInput(attrs={'class':'form-control','placeholder':'Voucher Number'}),
           'if_manual_entry': forms.CheckboxInput(attrs={'class':'form-check-input'}),
           'credit_sl': forms.Select(attrs={'class':'form-select'}),

           'debit_sl': forms.Select(attrs={'class':'form-select'}),
           'js_amount': forms.TextInput(attrs={'class':'form-control','placeholder':'Amount'}),
       }
   
    def clean(self):
        cleaned_data = super().clean()
        credit_sl = cleaned_data.get('credit_sl')
        debit_sl = cleaned_data.get('debit_sl')

        if credit_sl and debit_sl and credit_sl == debit_sl:
            raise forms.ValidationError("Ledger Account Head must be different.")
           

        return cleaned_data




   #  ===================================================
