from django.urls import path

from . import views

app_name = "Operations"

urlpatterns = [
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('muni', views.Muni, name='muni'),
    path('upload', views.Upload, name='upload'),
]
