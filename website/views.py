from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from users.models import User
from pizza.models import pizzas
from orders.models import count
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

def feedback(request):
    return render(request,"feedback.html")

def register(request):
    return render(request,"register.html")

def logout(request):
    del request.session["username"]
    return render(request,"login.html")

def menu(request):
    data = pizzas.objects.all()
    query = list(data.values())
    # render the menu page
    return render(request, "menu.html", {"menu": query})   
    
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
            data = pizzas.objects.all()
            query = list(data.values())
            return render(request, "home.html", {"username": username, "menu": query})
        else:
            # if no, then return error message
            return render(request, "login.html", {"error": "Invalid credentials"})
    else:
        # check if user is logged in
        if request.session.get("username"):
            # if yes, then show the home page
            username = request.session.get("username")
            data = pizzas.objects.all()
            query = list(data.values())
            return render(request, "home.html", {"username": username, "menu": query})
        else:
            # if no, then redirect to login page
            return render(request, "login.html", {"error": "Please login first"})
        
def modifymenu(request):
    if request.method == "POST":
        task = request.POST.get("task")
        name = request.POST.get("name")
        if (task == "add"):
            acutal_price = request.POST.get("actual_price")
            discounted_price = request.POST.get("discounted_price")
            image = request.POST.get("image")
            category = request.POST.get("category")
            discount = (int(acutal_price) - int(discounted_price))/int(acutal_price) * 100
            description = request.POST.get("description")
            # Check if the pizza already exists
            pizza = pizzas.objects.filter(name=name)
            if pizza:
                return render(request, "modifymenu.html", {"error": "Pizza with that name already exists"})
            else:
                pizza = pizzas(name=name, actual_price=acutal_price, discounted_price=discounted_price, image=image, category=category, discount=discount, description=description)
                pizza.save()
                return render(request, "modifymenu.html", {"error": "Pizza added successfully"})
        elif (task == "remove"):
            # Check if the pizza already exists
            pizza = pizzas.objects.filter(name=name)
            if pizza:
                pizza.delete()
                return render(request, "modifymenu.html", {"error": "Pizza with that name was removed successfully"})
            else:
                return render(request, "modifymenu.html", {"error": "Pizza does not exist"})
        else:
            return render(request, "modifymenu.html", {"error": "Invalid task"})
    else:
        return render(request,"modifymenu.html")
    
def buy(request):
    if request.method == "POST":
        name = request.session.get("username")
        # Check if orders have been placed before
        order = count.objects.filter(name=name)
        if order:
            # If yes, then update the count
            order = count.objects.get(name=name)
            order.count = order.count + 1
            order.save()
        else:
            # If no, then create a new entry
            order = count(name=name, count=1)
            order.save()
        return render(request, "buy.html", {"count": order.count, "msg": "Order placed successfully"})
    else:
        username = request.session.get("username")
        pid = request.GET.get("pizza")
        order = count.objects.filter(name=username)
        if order:
            pizza = pizzas.objects.get(id=pid)
            order = count.objects.get(name=username)
            return render(request, "buy.html", {"count": order.count, "msg": "", "pizza": pizza})
        else:
            pizza = pizzas.objects.get(id=pid)
            order = count(name=username, count=0)
            order.save()
            return render(request, "buy.html", {"count": order.count, "msg": "", "pizza": pizza})
