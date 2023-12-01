from django import forms

from item.models import *

class ItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    class Meta:
        model=Item
        exclude=['company']
        widgets={
            'itemCode': forms.TextInput(attrs={'class':'form-control item_search_input','placeholder':'Item Code'}),
            'itemName': forms.TextInput(attrs={'class':'form-control','placeholder':'Item Name'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'make': forms.TextInput(attrs={'class':'form-control','placeholder':'Make/Publisher'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Store Location'}),
            'vat': forms.TextInput(attrs={'class':'form-control','placeholder':'Vat %'}),
            'is_vatInclusive': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            }

class ItemBatchForm(forms.ModelForm):
    class Meta:
        model=ItemBatch
        exclude=['company','item','currentStock']
        widgets={
            'sales_rate': forms.TextInput(attrs={'class':'form-control','placeholder':'Sales Rate'}),
            'batch': forms.TextInput(attrs={'class':'form-control','placeholder':'Purchase Rate','readonly': 'readonly'}),
            'purchase_rate': forms.TextInput(attrs={'class':'form-control','placeholder':'Purchase Rate'}),
            'cost': forms.TextInput(attrs={'class':'form-control','placeholder':'Cost'}),
            'openingStock': forms.TextInput(attrs={'class':'form-control','placeholder':'Opening Stock'}),
            }