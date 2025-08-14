from django.shortcuts import render
from .models import Person


# Create your views here.

def personlar_royxati():
    persons = Person.objects.all()
    context = {
        'persons':persons
    }
    return render(request, 'persons.html', context)
