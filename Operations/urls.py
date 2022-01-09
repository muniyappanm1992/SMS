from django.urls import include, path

from . import views
from .router import router

app_name = "Operations"

urlpatterns = [
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('tterror', views.TTError, name='tterror'),
    path('indentstatus', views.IndentStatus, name='indentstatus'),
    path('muni', views.Muni, name='muni'),
    path('upload', views.Upload, name='upload'),
    path('officerhelp', views.OfficerHelp, name='officerhelp'),
    path('vendorhelp', views.VendorHelp, name='vendorhelp'),
    path('api/',include(router.urls)),
]
