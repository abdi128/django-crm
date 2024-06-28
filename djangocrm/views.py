from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if user logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authentiate user
        user=authenticate(request,username=username,password=password)
        #check if user is not empty
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully Logged in')
            return redirect('home')
        else:
            messages.success(request,'Something went wrong, Please try again')
            return redirect('home')
    else:  
         return render(request,'home.html',{})




def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})
