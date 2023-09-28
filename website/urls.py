from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"),
    path("header",header, name="header"),
    path("home",home,name="home"),
    path("about", about, name="about"),
]