from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse( 'This is Tutorial Page')

def index(request):
    return render(request, 'index.html')

def tutorial(request):
    return render(request, 'tutorial/tutorial.html')

def tutorial_details(request):
    return render(request, 'tutorial/tutorial_details.html')