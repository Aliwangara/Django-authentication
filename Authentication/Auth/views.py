from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import logging




# Create your views here.

def home(request):
    pass
    return render (request, "Home.html", )






def sign_up(request):
    if request.method == "POST":
        f_name = request.POST.get('FirstName')
        s_name = request.POST.get('LastName')
        mail = request.POST.get('email')
        Dob = request.POST.get('date')
        first_password = request.POST.get('pass1')
        second_password = request.POST.get('pass2')

        if first_password != second_password:
            messages.info(request, "password not matching")
            return redirect('/sign_up')

        try:
            if User.objects.get(username=mail):
                messages.warning(request, "Email Already Taken")

        except Exception as identifier:
            pass
        myuser = User.objects.create_user(mail, mail, first_password)
        myuser.save
        messages.success(request, "User Created Successfully")
        return redirect('Login')

    return render(request, "Signup.html")


def Log(request):
    if request.method == "POST":
        mail= request.POST.get('email')
        first_password= request.POST.get('pass1')
        myuser =authenticate(username= mail, password =first_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('home')
        else:
            messages.warning(request, "Invalid credentials")
    return render(request, "Login.html")