from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

    
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username,email=email,password=password)
                messages.success(request,"registration successfull!!!  Please login")
                return redirect('login')
            except:
                messages.error(request,"Username already exist!")
        else:
            messages.error(request,"Invalid username or password")
        return render(request,'register.html')


            

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')         
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'login.html')


def logout(request):
    return render('login')