from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        f_name = request.post.get('FirstName')
        s_name = request.post.get('LastName')
        mail = request.post.get('email')
        Dob = request.post.get('date')
        first_password = request.post.get('pass1')
        second_password = request.post.get('pass2')

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
        return redirect('signin')

    return render(request, "Signup.html")
