from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "authentication/login.html", {"message": None})
    context={
        "user": request.user
    }    
    return render(request,"calculateResults/index.html", context)

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "authentication/login.html", {"message": "invalid credentials!"})   

def logout_view(request):
    logout(request)
    return render(request, "authentication/login.html", {"message": "logged out."})