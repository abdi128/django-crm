from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    record=Record.objects.all()
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
         return render(request,'home.html',{'records':record})




def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
        
            login(request,user)
            messages.success(request,'You have successfully registered')
            return redirect('home')
            
    
    else:
        form =SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def details(request,key):
    if request.user.is_authenticated:
        record = Record.objects.get(id=key)
        context = {'record':record}

        return render(request,'details.html',context)
    else:
        messages.success(request,'You must have proper access to view this page')
        redirect('home')


def delete_record(request,key):
    if request.user.is_authenticated:
        record = Record.objects.get(id=key)
        record.delete()
        messages.success(request,'Record has been deleted successfully!')
        return redirect('home')
    
    else:
        messages.success(request,'You must have proper access to view this page')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,'You have successfully added a record')
                return redirect('home')
        
        return render(request,'add_record.html',{'form':form})
    
    else:
        messages.success(request,'You must have proper access to view this page')
        return redirect('home')
    
    
def update_record(request,key):
    if request.user.is_authenticated:
        record = Record.objects.get(id=key)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record has been updated')
            return redirect('home')
    
    
        return render(request,'update_record.html',{'form':form})
    
    else:
        messages.success(request,'Record has been updated')
        return redirect('home')

