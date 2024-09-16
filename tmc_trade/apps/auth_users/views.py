from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'auth_users/home_page.html')

def register(request):
    return render(request, 'auth_users/register.html')

def login(request):
    return render(request, 'auth_users/login.html')

def logout(request):
    return render(request, 'auth_users/home_page.html')

def profile(request):
    return render(request, 'auth_users/profile.html')