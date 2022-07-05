from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Question

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if User.objects.filter(username=username):
            messages.warning(request,"Username Already exists!!")
            return render(request,'signup.html')
        if User.objects.filter(email=email):
            messages.warning(request,'Email already registred')
            return render(request,'signup.html')
        if pass1!=pass2:
            messages.warning(request,'Password Not Matched')
            return render(request,'signup.html')
        else:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"You Account has been succesfully created")
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    pass

def signout(request):
    pass

def all_polls(request):
    pass

def vote(request):
    pass

def result(request):
    pass