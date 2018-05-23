from django.shortcuts import render
from .models import Cat
# Create your views here.

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]
