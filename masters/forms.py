from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=['company','user','customer_slno','customer_code']
        widgets={
            'customer_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Name'}),
            'customer_address1': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Address1'}),
            'customer_address2': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer address2'}),
            'customer_address3': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Addree3'}),
            'customer_phone1': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Phone1'}),
            'customer_phone2': forms.TextInput(attrs={'class':'form-control','placeholder':'Customer Phone2'}),
            'customer_trn': forms.TextInput(attrs={'class':'form-control','placeholder':'TRN'}),
            'customer_ob_amount': forms.NumberInput(attrs={'class':'form-control','placeholder':'Opening Balance'}),
            'customer_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'customer_ob_date': forms.DateInput(attrs={'class':'form-control','placeholder':'Opening Date'}),

    }
        
        