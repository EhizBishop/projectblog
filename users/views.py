from ast import Not
from operator import imod
from django.shortcuts import redirect, render
from . models import User

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate

from . forms import UserRegister
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST,request.FILES, None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email   = form.cleaned_data.get('email')
            password    = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if User.objects.filter(username = username):
                messages.warning(request, 'Username already exist !')
                return redirect('register')
            if User.objects.filter(email = email):
                messages.warning(request, 'Email already taken !')
                return redirect('register')

            if password != password2:
                messages.warning(request, 'Password not match!')
                return redirect('register')

            user = User.objects.create_user(username,email,password)
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request, 'User registered successfully !')
            return redirect('login')
            
        
    context={
        'form':form
    }
    return render(request, 'users/register.html',context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        users = authenticate(username = username, password = password)
        if users is not None:
            login(request,users)
            messages.success(request,'User logged in successfully !')
            return redirect('home')

        else:
            messages.warning(request,'username/password not correct !')


    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.warning(request,'user logged out successfully !')
    return redirect('login')


def userprofile(request):
    return render(request, 'users/userdashboard.html')