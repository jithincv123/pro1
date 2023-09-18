from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpass=request.POST["cpassword"]

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                    user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                    user.save()
                    return redirect('login')

        else:
             messages.info(request, "password not matching")
             return redirect('register.html')
    return render(request,"register.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
    return  render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")