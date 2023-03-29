from django.shortcuts import render
from .models import sign_in

# Create your views here.


def sign_in1(request):
    x=request.POST.get('username')
    y=request.POST.get('password')
    print(x)
    print(y)
    data = sign_in(username=x  , password=y)
    
    return render(request, 'sign_in.html')
    



def sign_up(request):
    return render(request, 'sign_up.html')
