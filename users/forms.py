from django import forms

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *

class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'s ou', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'s ou','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'s ou', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'s ou', 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class UserPermissionForm (forms.ModelForm):
    thumb = forms.ImageField(label='Attach a Photograph',widget=forms.FileInput(attrs={'class':'s ou mt-2'}))
    staff = forms.ModelChoiceField(queryset=Employee.objects.filter(is_staff_left=False), widget=forms.Select(attrs={'class':'s ou w-50'}))
    class Meta:
        model = UserPermission
        fields = ('thumb','company','permission','staff')

        widgets = {
            'company': FilteredSelectMultiple(verbose_name="Company",is_stacked=False,),
            'permission': FilteredSelectMultiple(verbose_name="Permission", is_stacked=False,) }
    


class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username', 'class':'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))