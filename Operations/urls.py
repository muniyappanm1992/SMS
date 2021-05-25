from django.urls import path

from . import views

app_name = "Operations"

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('muni', views.Muni, name='muni'),
    path('dryout', views.Dryout, name='dryout'),
]
