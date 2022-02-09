from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        v1 = request.POST['username']
        v2 = request.POST['first_name']
        v3 = request.POST['last_name']
        v4 = request.POST['email']
        v5 = request.POST['password']
        v6 = request.POST['password1']
        if v5 == v6:
            if User.objects.filter(username=v1).exists():
                messages.info(request, "Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=v4).exists():
                messages.info(request, "Email ID already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=v1, password=v5, first_name=v2, last_name=v3, email=v4)
                user.save()
                print("Uer Created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        v1 = request.POST['username']
        v5 = request.POST['password']
        user = auth.authenticate(username=v1, password=v5)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "User name and password is incorrect")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
