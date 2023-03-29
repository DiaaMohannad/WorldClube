from django.shortcuts import render
from django.http import HttpResponse
from country.models import People, Custom , Food, Event


# Create your views here.


def home(request):
     x = {'people': People.objects.all()[:3]  }
     return render(request , 'home.html' , x)


def log_in(request):
    return render(request , 'log_in.html')


def sign_up(request):
    return render(request , 'sign_up.html')


    