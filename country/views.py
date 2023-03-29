from django.shortcuts import render
from .models import People, Custom, Event, Food

# Create your views here.


def country(request):
    x = {'people': People.objects.all()}
    return render(request, 'country.html', x)


def country1(request):
    x = {'event': Event.objects.get(people_id=People.objects.get(id=2)),
         'custom': Custom.objects.get(id=2),
         'people': People.objects.get(id=2),
         'food': Food.objects.get(id=2), }
    return render(request, 'country1.html', x)


def index(request, id):
    if id == 4:
        y = {'event': Event.objects.get(people_id=People.objects.get(id=id)),
             'custom': Custom.objects.get(id=5),
             'people': People.objects.get(id=id),
             'food': Food.objects.get(id=id), }
        
    else:
        y = {'event': Event.objects.get(people_id=People.objects.get(id=id)),
             'custom': Custom.objects.get(id=id),
             'people': People.objects.get(id=id),
             'food': Food.objects.get(id=id), }


    return render(request, 'index.html', y)
