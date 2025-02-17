from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                username = request.POST["username"],
                first_name = request.POST["first_name"],
                last_name = request.POST["last_name"],
                email = request.POST["email"],
                password = request.POST["password"]
            )
            user.save()

            return redirect("users_app:signin")
        except:
            msg = "Username taken!"

    return render(request, 'users_app/signup.html', {"msg" : msg})


def signin(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user : User = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user:
            login(request, user)
            return redirect("main_app:home")
        else:
            msg = "Incorrect Credentials"

    return render(request, 'users_app/signin.html', {"msg" : msg})


def signout(request: HttpRequest):
    logout(request)

    return redirect('main_app:home')


def no_permission(request: HttpRequest):
    return render(request, "users_app/no_permission.html")