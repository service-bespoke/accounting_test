from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView

# Index page

class Index(LoginRequiredMixin,TemplateView):
   login_url = 'users:login'
   template_name = 'dashboard.html'