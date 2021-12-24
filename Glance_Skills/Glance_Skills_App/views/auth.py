from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views.generic import View

from Glance_Skills_App.models import extendeduser
from Glance_Skills_App.forms import LoginForm,SignupForm,UserEditForm

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            "form":form
        }
        return render(request,'auth/login.html',context=context)
        
    def post(self,request):
        form = LoginForm(request=request,data=request.POST)
        context = {
            "form":form
        }
        if form.is_valid():
            return redirect("/")
        return redirect('/login')


class RegisterView(View):
    def get(self,request):
        form = SignupForm()
        forms = UserEditForm()
        return render(request,'auth/register.html',{'form':form,'forms':forms})
    
    def post(self,request):
        form = SignupForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            user = form.save()
            forms = extendeduser.objects.create(user=user,phone_number=request.POST['phone_number'])
            forms.save()
            if user is not None:
                messages.success(request,"Account Created , Please Check your Email ID !")
                return redirect('login')
        return render(request,'auth/register.html',{'form':form,'forms':forms})

class ResetPasswordPage(View):

    def get(self,request):
        return render(request,'auth/reset-password.html')

    def post(self,request):
        return render(request,'auth/reset-password.html')


def LogoutView(request):
    logout(request)
    return redirect('home')