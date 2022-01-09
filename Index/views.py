import pandas as pd
import requests
import sqlalchemy
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from Index.models import ImageModel

from .forms import ImageForm


# Create your views here.
def index(request):
    t=ImageModel.objects.get(id=1)
    if "GET" == request.method:
        imagenamelist=[]
        for i in range(27):
            imagenamelist.append(str(i+1))
        caption="Indian Oil Sankari Terminal"
        mydict=model_to_dict(t)
        mydict.pop("id")
        arg={"imagenamelist":imagenamelist,"caption":caption,"mydict":mydict}
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
def Dashboard(request):
    return render(request,'Index/dashboard.html')
def Image(request):
    if request.user.is_superuser:
        t=ImageModel.objects.get(id=1)
        form=ImageForm(instance=t)
        print('form',form)
        if "GET" == request.method:
            imagenamelist=[]
            for i in range(27):
                imagenamelist.append(str(i+1))
            mydict=model_to_dict(t)
            mydict.pop("id")
            arg={"imagenamelist":imagenamelist,"mydict":mydict,"form":form}
            return render(request,'Index/ImageUpload.html',arg)
        elif "POST" == request.method:
            form = ImageForm(request.POST,request.FILES,instance=t)
            print('post-form',form)
            if form.is_valid():
                form.save()
                print('form valid')
            form=ImageForm(instance=t)
            imagenamelist=[]
            for i in range(27):
                imagenamelist.append(str(i+1))
            mydict=model_to_dict(t)
            mydict.pop("id")
            arg={"imagenamelist":imagenamelist,"mydict":mydict,"form":form}
            return render(request,'Index/ImageUpload.html',arg)
    else:
        return redirect("/")
