from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        user = authenticate(username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        cpwd = request.POST.get("confirm_password")

        # validation
        if pwd != cpwd:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=uname, email=email, password=pwd)
        user.save()

        messages.success(request, "Successfully Registered! Please Login.")
        return redirect("login")

    return render(request, "register.html")


def home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "home.html")


def logout_user(request):
    logout(request)
    return redirect("login")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user
    return render(request, "profile.html", {"user": user})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def edit_profile(request):
    user = request.user   

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")


        if username == "" or username is None:
            messages.error(request, "Username cannot be empty.")
            return redirect('edit_profile')

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        user.save()  
        messages.success(request, "Profile updated successfully!")

        return redirect('profile')

    return render(request, "edit_profile.html")

