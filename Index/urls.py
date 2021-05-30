from django.urls import path

from . import views

app_name = "Index"

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('upload', views.Upload, name='upload'),
    path('', views.index, name='index'),
    path('dev', views.Dev, name='index'),
]
