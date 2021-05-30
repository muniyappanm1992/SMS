from django.urls import path

from . import views

app_name = "QCModule"

urlpatterns = [
    # path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('upload', views.Upload, name='upload'),
    path('', views.index, name='index'),
]
