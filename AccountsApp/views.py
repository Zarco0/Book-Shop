from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def UserRegistration(request):

    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists')
                return redirect('webaccount:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Registered')
                return redirect('webaccount:register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
            return redirect('webaccount:login')
        else:
            messages.info(request,'Password Not Matching')
    return render(request,'accounts/register.html')


def Login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('webuser:listbook')
        else:
            messages.info(request,'Password or Username Incorrect ! Check again..')
            return redirect('webaccount:login')
        
    return render(request,'accounts/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('webaccount:login')