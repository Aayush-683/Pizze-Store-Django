from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from users.models import User
from pizza.models import pizzas
# Create your views here.

def login(request):
    # check if its a post request
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check if username and password are in database
        user = User.objects.filter(username=username)
        if user:
            return render(request, "register.html", {"error": "Username already exists"})
        else:
            user = User(username=username, password=password)
            user.save()
            return render(request, "login.html", {"error": "Account created successfully. Please login."})
    else:
        return render(request, "login.html")

def about(request):
    return render(request,"about.html")

def header(request):
    return render(request,"header.html")

def contact(request):
    return render(request,"contact.html")

def register(request):
    return render(request,"register.html")

def logout(request):
    del request.session["username"]
    return render(request,"login.html")

def menu(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        # check if username and password are in database
        menu = pizzas.objects.filter(name=name)
        if menu:
            return render(request, "menu.html", {"error": "menu already exists"})
        else:
            menu = pizzas(name=name, price=price)
            pizzas.save()
            return render(request, "menu.html", {"error": "menu created successfully. Please login."})
    else:
        data = pizzas.objects.all()
        query = list(data.values())
        # render the menu page
        return render(request, "menu.html", {"menu": query})

# make a post request handler for login
# make a post request handler for register    
    
def home(request):
    # check if its a post request
    if request.method == "POST":
        # get the username and password
        username = request.POST.get("username")
        password = request.POST.get("password")
        # check if username and password are in database
        user = User.objects.filter(username=username, password=password)
        if user:
            # if yes, then login the user
            request.session["username"] = username
            return render(request, "home.html", {"username": username})
        else:
            # if no, then return error message
            return render(request, "login.html", {"error": "Invalid credentials"})
    else:
        # check if user is logged in
        if request.session.get("username"):
            # if yes, then show the home page
            username = request.session.get("username")
            return render(request, "home.html", {"username": username})
        else:
            # if no, then redirect to login page
            return render(request, "login.html", {"error": "Please login first"})
        
def modifymenu(request):
    return render(request,"modifymenu.html")