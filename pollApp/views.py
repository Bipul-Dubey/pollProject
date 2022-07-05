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
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST['password']

        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('all_polls')
        else:
            messages.error(request,'Bad Credential!')
            return redirect('signin')
    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,'You are successfully logout')
    return redirect('signup')

def all_polls(request):
    current_user = request.user
    username=current_user.username
    questions=Question.objects.all()
    print(questions)
    return render(request,'all_polls.html',{'questions':questions,'username':username})

def vote(request,id):
    poll_que_data=Question.objects.filter(id=id).values_list('question','opt1','opt2','opt3','opt4')
    poll_data_list=list(poll_que_data)
    question=poll_data_list[0][0]
    opt1=poll_data_list[0][1]
    opt2=poll_data_list[0][2]
    opt3=poll_data_list[0][3]
    opt4=poll_data_list[0][4]
    poll_data={
        'question':question,
        'options':[opt1,opt2,opt3,opt4]
    }
    return render(request,'vote.html',{'poll':poll_data})

def result(request):
    pass

def addquestion(request):
    if request.method=='POST':
        ques=request.POST['question']
        opt1=request.POST['opt1']
        opt2=request.POST['opt2']
        opt3=request.POST['opt3']
        opt4=request.POST['opt4']
        question_data=Question(question=ques,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4)
        question_data.save()
    return render(request,'addquestion.html')