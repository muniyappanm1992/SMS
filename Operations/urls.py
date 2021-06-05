from django.urls import path, include

from . import views
from .router import router
app_name = "Operations"

urlpatterns = [
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('muni', views.Muni, name='muni'),
    path('upload', views.Upload, name='upload'),
    path('api/',include(router.urls)),
]
