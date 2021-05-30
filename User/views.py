from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,auth
# Create your views here.
def Register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            firstName = form.cleaned_data.get('first_name')
            return render(response, "User/register_confirmation.html", {"firstName":firstName})
    else:
        form = RegisterForm()
    return render(response, "User/register.html", {"form":form})

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth.login(request,user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request,'User/login.html',{"form":form})
def logout(request):
    auth.logout(request)
    return redirect("/")