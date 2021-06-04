from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    if "GET" == request.method:
        imagenamelist=[]
        for i in range(27):
            imagenamelist.append(str(i+1))
        caption="Indian Oil Sankari Terminal"
        arg={"imagenamelist":imagenamelist,"caption":caption}
        return render(request, 'Index/index.html',arg)
def login(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth.login(request,user)
            return redirect("/")
    else:
        return redirect("/")
    return render(request,'User/login.html',{"form":form})

def logout(request):
    auth.logout(request)
    return redirect("/")
def Dev(request): # under development
    return render(request,'Index/dev.html')