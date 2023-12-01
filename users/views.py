from django.shortcuts import render
from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView

from django.contrib import messages

from .models  import *
from .forms import *


def getLoginCompany(user):
    loginCompany=LoginCompany.objects.get(user=user)
    return loginCompany.company

def notifications(user,description):
    company=getLoginCompany(user)
    notification=Notifications(company=company,
                               user=user,
                               description=description)
    notification.save()


# Create your views here.
class User_All(LoginRequiredMixin,ListView):
    template_name = 'authentication/index.html'
    model = UserPermission
    login_url = 'users:login'
    context_object_name = 'users'
    paginate_by  = 12

    # @method_decorator(permissions_required('user_creation'))
    # def dispatch(self, *args, **kwargs):
    #     return super(User_All, self).dispatch(*args, **kwargs)

#   Authentication

@login_required(login_url='users:login')
def Register(request):
    registration_form=RegistrationForm
    user_form=UserPermissionForm
    if request.method== 'POST':
        registration_dataform=RegistrationForm(request.POST)
        user_dataform=UserPermissionForm(request.POST,request.FILES)
        if registration_dataform.is_valid():
            reg=registration_dataform.save()
            if user_dataform.is_valid():
                user=User.objects.get(id=reg.id)
                user_data=user_dataform.save(commit=False)
                user_data.user=user
                user_data.save()
                user_dataform.save_m2m()
                notifications(request.user,"New User Created "+reg.username)
                return redirect('users:user_all')
            else:
                return render(request,'authentication/signup.html',{'registration_form':registration_dataform,'user_form':user_dataform})
        else:
            return render(request,'authentication/signup.html',{'registration_form':registration_dataform,'user_form':user_dataform})

    return render(request,'authentication/signup.html',{'registration_form':registration_form,'user_form':user_form})
    
@login_required(login_url='users:login')
def user_update(request,pk):
    user=User.objects.get(id=pk)
    user_profile=UserPermission.objects.get(user=user)
    user_form=UserPermissionForm(request.POST or None, instance=user_profile)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            notifications(request.user,"User Updated "+user_profile.user.username)
            return redirect('users:user_all')
        return render(request,'authentication/edit_user.html',{'user_form':user_form})
    return render(request,'authentication/edit_user.html',{'user_form':user_form})

class User_Update(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'authentication/edit_user.html'
    form_class = UserPermissionForm
    login_url = 'users:login'
    success_message = 'Updated Successfully'
    error_message = 'Error in form'
    success_url = reverse_lazy('users:user_all')

    def get_form_kwargs(self):
        form_class = super().get_form_kwargs()
        form_class['user'] = self.request.user
        return form_class
        
@login_required(login_url='users:login')        
def change_password(request,pk):
    user=User.objects.get(id=pk)
    if request.method =='POST':
        if user.is_superuser:
            messages.info(request, 'Password Cant Change.!')
        else:
            password1=request.POST['password1']
            password2=request.POST['password2']
            if password1 == password2:
                user.set_password(password1)
                user.save()
                notifications(request.user,"User Updated "+user.username)
                messages.info(request, 'Password Successfully Changed.')
            else:
                messages.info(request, 'Mismatch Passwords')
        return redirect('users:user_all')
    return render(request,'authentication/change_password.html')
    
@login_required(login_url='users:login')
def user_delete(request,pk):
    user=User.objects.get(id=pk)
    if user.is_superuser:
        messages.info(request, 'Password Cant Change.!')
    else:
        user.delete()
        notifications(request.user,"User Deleted "+user.username)
    messages.info(request, 'Successfully Removed User')
    return redirect('users:user_all')    

class Login_View(LoginView):
    model = User
    form_class = LoginForm
    template_name = 'authentication/signin.html'

    def get_success_url(self):
        url = resolve_url('users:login_company')
        return url
        
@login_required(login_url='users:login')
def selectCompany(request):
    user_company=UserPermission.objects.get(user=request.user)
    if request.method == 'POST':
        company=Company.objects.get(name=request.POST['company'])
        if LoginCompany.objects.filter(user=request.user).exists():
            login_company=LoginCompany.objects.get(user=request.user)
            login_company.company=company
            login_company.save()
        else:
            LoginCompany.objects.create(user=request.user,company=company)
        return redirect('dashboard:index')
    return render(request,'authentication/company.html',{'user_company':user_company})

class Logout_View(View):
    def get(self,request):
        logout(self.request)
        return redirect ('users:login',permanent=True)