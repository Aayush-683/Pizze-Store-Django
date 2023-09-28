from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"),
    path("header",header, name="header"),
    path("home",home,name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("register", register, name="register"),
    path("login_post", login_post, name="login_post"),
    path("register_post", register_post, name="register_post"),
]