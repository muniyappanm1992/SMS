from django.urls import path

from . import views

app_name = "Operations"

urlpatterns = [
    path('', views.index, name='index'),
    path('muni', views.Muni, name='muni'),
    path('dryout', views.Dryout, name='dryout'),
]
