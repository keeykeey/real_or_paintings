from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import Views

from .forms import LoginForm

class LoginView(View):
    def get(self,request,*args,**kwargs):
        """method for a GET request"
        context = {
            'form':LoginForm(),
        }
        
        return render(request,'accounts/login.html',context)


