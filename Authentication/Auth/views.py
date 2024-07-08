from django.shortcuts import render
from  django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        f_name = request.post.get('FirstName')
        s_name = request.post.get('LastName')
        mail = request.post.get('email')
        Dob = request.post.get('date')
        first_password = request.post.get('pass1')
        second_password = request.post.get('pass2')
        
        if first_password != second_password:
            message.info(request, "password not matching")
            
        

    
    return render(request, "Signup.html")
