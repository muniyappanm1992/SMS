from django.urls import path

from . import views

app_name = "User"


urlpatterns = [
    path('register', views.Register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
]
