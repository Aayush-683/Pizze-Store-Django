from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
# Create your views here.

def login(request):
    return render(request, "login.html", {"error": ""})

def header(request):
    return render(request,"header.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def register(request):
    return render(request,"register.html")

# make a post request handler for login
# make a post request handler for register


def login_post(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if (username == None or password == None):
        return render(request, "login.html", {"error": "Invalid username or password"})
    # check if username and password are in database
    user = User.objects.filter(username=username, password=password)
    if user:
        return render(request, "home.html")
    else:
        return render(request, "login.html", {"error": "Invalid username or password"})
    
def register_post(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    # check if username and password are in database
    user = User.objects.filter(username=username)
    if user:
        return render(request, "register.html", {"error": "Username already exists"})
    else:
        user = User(username=username, password=password, email=email)
        user.save()
        return render(request, "login.html", {"error": "Account created successfully. Please login."})