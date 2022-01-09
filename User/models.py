from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models.signals import post_save
from numpy import imag

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    phone=models.CharField(max_length=10,verbose_name='moblile number',validators=[RegexValidator(r'^\d{1,10}$')])
    designation=models.CharField(max_length=10,verbose_name='Designation')
    sign=models.ImageField(upload_to='sign',blank=False,verbose_name='Signature',default='blank.JPG')
    def __str__(self):
        return self.user.first_name
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
