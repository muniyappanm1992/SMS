from django.urls import path, include

from . import views
from .router import router
app_name = "QCModule"

urlpatterns = [
    # path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('upload', views.Upload, name='upload'),
    path('', views.index, name='index'),
    path('api/',include(router.urls)),
]
