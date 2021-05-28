from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    if "GET" == request.method:
        imagenamelist=[]
        for i in range(26):
            imagenamelist.append(i+1)
        caption="Indian Oil Sankari Terminal"
        arg={"imagenamelist":imagenamelist,"caption":caption}

        return render(request, 'Index/index.html',arg)


def login(request):
    if request.user.is_authenticated:
        return redirect("/qc/index")
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print("user=",user)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'Index/login.html')
    else:
        return render(request,'Index/login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")