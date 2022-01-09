from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.forms import ModelForm, fields

from .models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email", "password1", "password2"]

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields='__all__'
        exclude=['user']
