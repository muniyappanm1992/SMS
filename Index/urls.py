from django.urls import path

from . import views

app_name = "Index"

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('dev', views.Dev, name='under construction'),
    path('img', views.Image, name='img'),
]
