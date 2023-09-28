from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "login.html")

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